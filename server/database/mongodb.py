from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
from bson import ObjectId

class MongoDB:
    client: AsyncIOMotorClient = None
    database = None
    user_collection = None

    @classmethod
    async def connect_to_mongo(cls):
        cls.client = AsyncIOMotorClient("mongodb://localhost:27017")
        cls.database = cls.client.auth_db
        cls.user_collection = cls.database.users
        
        # Create unique index on email
        await cls.user_collection.create_index([("email", ASCENDING)], unique=True)

    @classmethod
    async def close_mongo_connection(cls):
        if cls.client:
            cls.client.close()
