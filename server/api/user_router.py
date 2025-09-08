from fastapi import APIRouter

from schemas.user import ResetRequest, ResetConfirm, UserCreate, UserLogin
from controllers.user_controller import request_password_reset, confirm_password_reset,register_user,login_user
    

router = APIRouter()

@router.post("/register")
async def register__user(user:UserCreate) -> dict:
    """
    Register a new user in the system.

    Parameters:
        user (UserCreate): The user's registration details.

    Returns:
        dict: A success message on successful registration.

    Raises:
        HTTPException: If the username already exists or a server error occurs.
    """
    return await register_user(user)


@router.post("/login")
async def login(user: UserLogin) -> dict:
    """
    Authenticate a user and return a JWT access token.

    Parameters:
        user (UserLogin): The user's login credentials.

    Returns:
        dict: A token and token type on successful login.

    Raises:
        HTTPException: If login credentials are invalid or a server error occurs.
    """
    return await login_user(user)


@router.post("/reset-password")
async def reset_password(request: ResetRequest) -> dict:
    """
    Request a password reset by providing a registered email.

    Parameters:
        request (ResetRequest): The user's email address.

    Returns:
        dict: A password reset token and message on success.

    Raises:
        HTTPException: If the email is not found or a server error occurs.
    """
    return await request_password_reset(request)


@router.post("/reset-password/confirm")
async def confirm_reset(request: ResetConfirm) -> dict:
    """
    Confirm password reset using the reset token and new password.

    Parameters:
        request (ResetConfirm): Contains the reset token and the new password.

    Returns:
        dict: A message confirming password reset on success.

    Raises:
        HTTPException: If the token is invalid, expired, or other errors occur.
    """
    return await confirm_password_reset(request)