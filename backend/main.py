from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from decay import decay

load_dotenv()

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
collection = db["memories"]

class MemoryCreate(BaseModel):
    content: str
    salience: float = 1.0

@app.post("/memories/")
async def create_memory(mem: MemoryCreate):
    doc = {
        "content": mem.content,
        "salience": mem.salience,
        "timestamp": datetime.utcnow().isoformat(),
        "last_accessed": datetime.utcnow().isoformat(),
        "pinned": False
    }
    result = await collection.insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

@app.get("/memories/")
async def get_memories(search: str = Query(None)):
    query = {}
    if search:
        query["content"] = {"$regex": search, "$options": "i"}

    cursor = collection.find(query)
    memories = []
    async for mem in cursor:
        # Update last_accessed when memory is fetched
        await collection.update_one(
            {"_id": mem["_id"]},
            {"$set": {"last_accessed": datetime.utcnow().isoformat()}}
        )
        # Apply decay if not pinned
        if not mem.get("pinned", False):
            mem["salience"] = decay(mem["salience"], mem["timestamp"])
        mem["_id"] = str(mem["_id"])
        memories.append(mem)
    return memories

@app.patch("/memories/{memory_id}/pin")
async def pin_memory(memory_id: str):
    result = await collection.update_one({"_id": ObjectId(memory_id)}, {"$set": {"pinned": True}})
    if result.matched_count:
        return {"message": "Memory pinned"}
    raise HTTPException(status_code=404, detail="Memory not found")

@app.patch("/memories/{memory_id}/unpin")
async def unpin_memory(memory_id: str):
    result = await collection.update_one({"_id": ObjectId(memory_id)}, {"$set": {"pinned": False}})
    if result.matched_count:
        return {"message": "Memory unpinned"}
    raise HTTPException(status_code=404, detail="Memory not found")

@app.delete("/memories/{memory_id}")
async def delete_memory(memory_id: str):
    result = await collection.delete_one({"_id": ObjectId(memory_id)})
    if result.deleted_count:
        return {"message": "Memory deleted"}
    raise HTTPException(status_code=404, detail="Memory not found")

@app.get("/old_memories/")
async def get_old_memories(days: int = 30):
    """List memories not accessed in the last `days` days"""
    cutoff = datetime.utcnow() - timedelta(days=days)
    cursor = collection.find({
        "last_accessed": {"$lt": cutoff.isoformat()},
        "pinned": False
    })
    old_memories = []
    async for mem in cursor:
        mem["_id"] = str(mem["_id"])
        old_memories.append(mem)
    return old_memories
