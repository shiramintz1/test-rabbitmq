
#save in the db
from datetime import datetime

class User:
    def __init__(self, id: str, username: str,full_name: str, email: str, hashed_password: str, created_at: datetime):
        self.id = id
        self.username = username
        self.full_name = full_name
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = created_at
    #The fields that will actually be stored in the conditions database
    def to_dict(self):
        return {
            "_id": self.id,
            "username": self.username,
            "full_name": self.full_name,
            "email": self.email,
            "hashed_password": self.hashed_password,
            "created_at": self.created_at
        }