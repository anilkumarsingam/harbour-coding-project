from fastapi import FastAPI
from pymongo import MongoClient
from app.api.schedules import schedules
import os

app = FastAPI(openapi_url="/api/v1/schedules/openapi.json", docs_url="/api/v1/schedules/docs")

@app.on_event("startup")
async def startup_db_client():

    MONGO_URI = os.getenv('MONGO_URI') 
    DB_NAME = os.getenv('DB_NAME')
    app.mongodb_client = MongoClient(MONGO_URI)
    app.database = app.mongodb_client[DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    await app.mongodb_client.close()

app.include_router(schedules, prefix="/api/v1/schedules", tags=["schedules"])
