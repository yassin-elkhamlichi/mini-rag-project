from fastapi import FastAPI, APIRouter
import os


base_router = APIRouter(
    prefix="/welcome",
    tags=["api_for_testing"]  
)

@base_router.get("/")
def welcome():
    return {
        "message" : "Hello World!"
    }

@base_router.get("/name")
async def name():
    return {
        "name" : os.getenv("APP_NAME")
    }

@base_router.get("/version")
def version():
     return {
        "APP VERSION" : os.getenv("APP_VERSION")
    }

