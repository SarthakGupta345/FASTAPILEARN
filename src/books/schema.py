from pydantic import BaseModel

class BookUpdate(BaseModel):
    title: str
    language: str

class BookModel(BaseModel):
    id: int
    title: str
    author: str
    language: str

