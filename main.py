from fastapi import FastAPI,HTTPException,Query
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

# dynamic query parameter passed in normal ways


@app.get('/greet/{name}')
async def greet(name:str)->dict:
    return {'message':f'Hello {name}'}


#query field passed by /?name=
@app.get('/greet')
async def greet2(name:str)->dict:
    return {'message':f'Hello {name} newone '}