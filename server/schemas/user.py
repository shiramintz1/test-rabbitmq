from pydantic import BaseModel, EmailStr, Field
from typing import Optional

#The fields that the customer is expected to enter during registration
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=2)
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserInDB(UserCreate):
    hashed_password: str

#The fields that the customer is expected to enter when logging in
class UserLogin(BaseModel):
    username: str
    password: str

#The fields that will be displayed to the customer when requesting to view customer details
class UserResponse(BaseModel):
    id: str
    username: str
    full_name: str
    email: EmailStr
    created_at: Optional[str] = None
#The fields that the customer is expected to enter in a password reset request
class ResetRequest(BaseModel):
    email: EmailStr
#The fields that the customer is expected to enter in the confirmation and reset request
class ResetConfirm(BaseModel):
    token: str
    new_password: str