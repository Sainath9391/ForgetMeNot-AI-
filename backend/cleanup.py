import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
collection = db["memories"]

async def cleanup_old_memories(days=30):
    cutoff = datetime.utcnow() - timedelta(days=days)
    old_memories = await collection.find({"last_accessed": {"$lt": cutoff.isoformat()}}).to_list(None)

    for mem in old_memories:
        print(f"🛑 Deleting unused memory: \"{mem['content']}\" (last used: {mem['last_accessed']})")
        await collection.delete_one({"_id": mem["_id"]})
    print(f"✅ Cleanup complete. Deleted {len(old_memories)} memories.")

if __name__ == "__main__":
    asyncio.run(cleanup_old_memories())
