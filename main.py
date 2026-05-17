from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(
    title="Learning FastAPI",
    description='This is my first ffastapi web backend',
    version='1.0'
)

@app.get('/')
async def root()->dict:
    return {'message':'Hello world'}

@app.get("/check")
async def check()->dict:
    return {'message':'Server is running properly'}