
from datetime import timedelta,datetime
from fastapi import HTTPException
from jwt.exceptions import ExpiredSignatureError, DecodeError,InvalidTokenError
import logging
import uuid

from models.user import User 
from schemas.user import UserCreate,UserLogin,ResetConfirm,ResetRequest
from services.database import users_collection
from utils.hash import hash_password,verify_password
from utils.jwt import create_access_token,decode_token

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

#register_user
async def register_user(user_data:UserCreate) -> dict:
    try:
        logger.info(f"Registering user: {user_data.username}")
        existing_user=await users_collection.find_one({"username": user_data.username})
        if existing_user:
            logger.warning(f"Username '{user_data.username}' already exists")
            raise HTTPException(status_code=400,detail="username already exists")
        
        #Password encryption
        hashed_pwd=hash_password(user_data.password)
        # Create a user object with an encrypted password to save in the database
        user_obj = User(
            id=str(uuid.uuid4()), 
            username=user_data.username,
            full_name=user_data.full_name,
            email=user_data.email,
            hashed_password=hashed_pwd,
            created_at=datetime.utcnow()
        )
        await users_collection.insert_one(user_obj.to_dict())
        logger.info(f"User '{user_data.username}' registered successfully")
        return {"message": "User registered successfully"}

    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error(f"Error registering user '{user_data.username}': {e}")
        raise HTTPException(status_code=500, detail="Server error while registering user")

#login_user
async def login_user(user_data:UserLogin) -> dict:
    try:
        logger.info(f"User login: {user_data.username}")
        user = await users_collection.find_one({"username": user_data.username})
        if not user or not verify_password(user_data.password, user["hashed_password"]):
             logger.warning(f"Invalid login for username: {user_data.username}")
             raise HTTPException(status_code=400, detail="Invalid username or password")  
        
        token=create_access_token(
            data={"sub":user["username"]},
            expires_delta=timedelta(minutes=60)
            )
        logger.info(f"User '{user_data.username}' logged in successfully")
        return {"token":token, "token_type": "bearer"}

    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error(f"Login error for '{user_data.username}': {e}")
        raise HTTPException(status_code=500, detail="Server error during login")


#Password reset
# Step 1 – Sending a token (Let's assume in the future he will send it by email)
async def request_password_reset(request: ResetRequest) -> dict:
    try:
        logger.info(f"Password reset requested for email: {request.email}")
        user = await users_collection.find_one({"email": request.email})
        if not user:
            logger.warning(f"Password reset: Email not found: {request.email}")
            raise HTTPException(status_code=404, detail="User with this email not found")

        # Creating a token with a short validity period
        token = create_access_token(
            data={"sub": user["username"]}, 
            expires_delta=timedelta(minutes=15)
            )
        logger.info(f"Password reset token created for user: {user['username']}")
        # TODO:Sending the token by email (in the meantime, they returned it as a response)
        return {"reset_token": token, "message": "Password reset link sent to email"}

    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error(f"Error in password reset request for {request.email}: {e}")
        raise HTTPException(status_code=500, detail="Server error during password reset request")

# Step 2 – Token Verification and Password Reset
async def confirm_password_reset(request: ResetConfirm) -> dict:
    try:
        logger.info("Confirming password reset using token")
        payload = decode_token(request.token)
        username = payload.get("sub")
        if not username:
            logger.warning("Invalid token payload – missing 'sub'")
            raise HTTPException(status_code=400, detail="Invalid token data")

        hashed = hash_password(request.new_password)
        result = await users_collection.update_one(
            {"username": username}, 
            {"$set": {"hashed_password": hashed}}
            )

        if result.modified_count == 0:
            logger.warning(f"Password reset failed: user '{username}' not found or password not changed")
            raise HTTPException(status_code=404, detail="User not found or password not changed")

        logger.info(f"Password reset successful for user '{username}'")
        return {"message": "Password has been reset successfully"}

    except ExpiredSignatureError:
        logger.warning("Invalid or expired token")
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    except (DecodeError, InvalidTokenError):
        logger.warning("Invalid or expired token")
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    #The specific errors caught earlier will continue as they are
    # (without this they would be caught in the general exception and thrown as a server problem)
    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error(f"Error during password reset confirmation: {e}")
        raise HTTPException(status_code=500, detail="Server error during password reset")            



