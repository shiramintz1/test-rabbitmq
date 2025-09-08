from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db_name = os.getenv("DB_NAME", "mock_db") 
db = client[db_name]
users_collection = db["users"]