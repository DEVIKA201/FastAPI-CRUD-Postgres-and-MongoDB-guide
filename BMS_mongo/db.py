from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://devika:sh221b@localhost:27017/bms_db?authSource=bms_db")
db = client.bms_db
