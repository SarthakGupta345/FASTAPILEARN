from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

class BookModel(BaseModel):
    id: int
    title: str
    author: str
    language: str


books = [
    {
        "id": 23,
        "title": "Harry potter",
        "author": "chandan gupta",
        "language": "english"
    },
    {
        "id": 24,
        "title": "Games of thrones",
        "author": "chandan gupta",
        "language": "english"
    },
    {
        "id": 25,
        "title": "The boys",
        "author": "chandan gupta",
        "language": "english"
    }
]


class BookUpdate(BaseModel):
    title: str
    language: str


app = FastAPI()


@app.get('/books', status_code=200, response_model=List[BookModel])
async def get_books():
    return books


@app.post('/createbook', status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookModel) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in books:
        if book_id == book['id']:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Book not found'
    )


@app.delete('/book/{book_id}', status_code=status.HTTP_200_OK)
async def delete_book(book_id: int):
    for book in books:
        if book_id == book['id']:
            books.remove(book)
            return {'message': 'Book deleted successfully'}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Book not found'
    )


@app.patch('/updateBook/{book_id}')
async def update_book(book_id: int, book_data: BookUpdate):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_data.title
            book['language'] = book_data.language
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Book not found'
    )