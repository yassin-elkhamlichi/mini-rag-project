from fastapi import FastAPI
from routes import base_router
from routes import data_router
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import Settings, get_setting
app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    settings = get_setting()
    app.mongodb_client = AsyncIOMotorClient(settings.mongodb_uri)
    app.db_client = app.mongodb_client[settings.DB_NAME]

app.include_router(base_router)
app.include_router(data_router)

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
    print("DB connection closed.")