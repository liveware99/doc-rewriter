
from fastapi import FastAPI
from app.api import rewrite
import os

app = FastAPI()
app.include_router(rewrite.router)

# Create folders if not present
os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)
os.makedirs("templates", exist_ok=True)
