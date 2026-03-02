from fastapi import FastAPI, APIRouter, Depends
from helpers import getSetting, Settings


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
def name(app_settings: Settings = Depends(getSetting)):
    return {
        "name" : app_settings.APP_NAME
    }

@base_router.get("/version")
def version(app_settings: Settings = Depends(getSetting)):
     return {
        "APP VERSION" : app_settings.APP_VERSION
    }

