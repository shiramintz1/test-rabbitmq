
import pytest
from fastapi import HTTPException
from schemas.user import UserCreate, UserLogin, ResetRequest, ResetConfirm
from controllers import user_controller
from utils.hash import hash_password
from unittest.mock import AsyncMock
from jwt.exceptions import DecodeError


@pytest.mark.asyncio
async def test_register_user_success(mocker):
    mocker.patch("services.database.users_collection.find_one", new_callable=AsyncMock, return_value=None)
    mocked_insert = mocker.patch("services.database.users_collection.insert_one", new_callable=AsyncMock)

    user = UserCreate(
        username="testuser",
        full_name="Test User",
        email="test@example.com",
        password="12345678" 
    )

    result = await user_controller.register_user(user)
    assert result == {"message": "User registered successfully"}
    mocked_insert.assert_called_once()

@pytest.mark.asyncio
async def test_register_user_username_exists(mocker):
    mocker.patch("services.database.users_collection.find_one", new_callable=AsyncMock, return_value={"username": "testuser"})

    user = UserCreate(
        username="testuser",
        full_name="Test User",
        email="test@example.com",
        password="12345678"
    )

    with pytest.raises(HTTPException) as e:
        await user_controller.register_user(user)
    assert e.value.status_code == 400
    assert e.value.detail == "username already exists"

@pytest.mark.asyncio
async def test_login_user_success(mocker):
    hashed = hash_password("12345678")
    mocker.patch("services.database.users_collection.find_one", new_callable=AsyncMock, return_value={"username": "testuser", "hashed_password": hashed})

    user = UserLogin(username="testuser", password="12345678")

    result = await user_controller.login_user(user)
    assert "token" in result
    assert result["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_user_wrong_password(mocker):
    hashed = hash_password("abcdefghi")
    mocker.patch("services.database.users_collection.find_one", new_callable=AsyncMock, return_value={"username": "testuser", "hashed_password": hashed})

    user = UserLogin(username="testuser", password="wrongpass")

    with pytest.raises(HTTPException) as e:
        await user_controller.login_user(user)
    assert e.value.status_code == 400

@pytest.mark.asyncio
async def test_login_user_invalid_username(mocker):
    mocker.patch("services.database.users_collection.find_one", new_callable=AsyncMock, return_value=None)

    user = UserLogin(username="unknown_user", password="12345678")

    with pytest.raises(HTTPException) as e:
        await user_controller.login_user(user)
    assert e.value.status_code == 400
    assert e.value.detail == "Invalid username or password"

@pytest.mark.asyncio
async def test_request_password_reset_success(mocker):
    mocker.patch("services.database.users_collection.find_one", new_callable=AsyncMock, return_value={"username": "testuser", "email": "test@example.com"})

    request = ResetRequest(email="test@example.com")

    result = await user_controller.request_password_reset(request)
    assert "reset_token" in result
    assert result["message"] == "Password reset link sent to email"

@pytest.mark.asyncio
async def test_request_password_reset_invalid_email(mocker):
    mocker.patch("services.database.users_collection.find_one", new_callable=AsyncMock, return_value=None)

    request = ResetRequest(email="nonexistent@example.com")

    with pytest.raises(HTTPException) as e:
        await user_controller.request_password_reset(request)
    assert e.value.status_code == 404
    assert e.value.detail == "User with this email not found"

@pytest.mark.asyncio
async def test_confirm_password_reset_success(mocker):
    mocker.patch("controllers.user_controller.decode_token", return_value={"sub": "testuser"})
    mock_update = mocker.patch("services.database.users_collection.update_one", new_callable=AsyncMock)
    mock_update.return_value.modified_count = 1

    request = ResetConfirm(token="valid_token", new_password="newpass123")

    result = await user_controller.confirm_password_reset(request)
    assert result["message"] == "Password has been reset successfully"

@pytest.mark.asyncio
async def test_confirm_password_reset_invalid_token(mocker):
    mocker.patch("controllers.user_controller.decode_token", side_effect=DecodeError("bad token", "", 0))

    request = ResetConfirm(token="invalid", new_password="12345678")

    with pytest.raises(HTTPException) as e:
        await user_controller.confirm_password_reset(request)
    assert e.value.status_code == 400
    assert e.value.detail == "Invalid or expired token"

@pytest.mark.asyncio
async def test_confirm_password_reset_expired_token(mocker):
    from jwt.exceptions import ExpiredSignatureError
    mocker.patch("controllers.user_controller.decode_token", side_effect=ExpiredSignatureError("Signature has expired"))

    request = ResetConfirm(token="expired_token", new_password="newpass123")

    with pytest.raises(HTTPException) as e:
        await user_controller.confirm_password_reset(request)
    assert e.value.status_code == 400
    assert e.value.detail == "Invalid or expired token"
