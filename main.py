from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from routes import basic_routes





app = FastAPI()

app.include_router(basic_routes.base_router)