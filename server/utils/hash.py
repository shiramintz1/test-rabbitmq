#Password encryption
import bcrypt

#A function to create an encrypted string of the password that will be stored in the database.
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

#A function for the login pen to check the correctness of the password against the password stored in the database 
#(since the password in the database is stored encrypted, there is no possibility of normal comparison)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))