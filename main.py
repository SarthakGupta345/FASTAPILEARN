from fastapi import FastAPI,HTTPException,Query,Header
from typing import Optional
from pydantic import BaseModel
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

# dynamic path parameter passed in normal ways


@app.get('/greet/{name}')
async def greet(name:str,age:Optional[int]=80)->dict:
    return {'message':f'Hello {name} your age is {age}'}


#dynamic query field passed by /?name=
@app.get('/greet')
async def greet2(name:str)->dict:
    return {'message':f'Hello {name} newone '}

class BookCreatemodel(BaseModel):
    title:str
    author:str

@app.post('/createBook')
async def create_book(bookData:BookCreatemodel):
    return {
        'message':'book created succesfully',
        'title':bookData.title
    }


@app.get('/get_headers')
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None)
):
    request_headers ={}
    request_headers['Accept'] = accept
    request_headers['content_type'] = content_type
    return request_headers