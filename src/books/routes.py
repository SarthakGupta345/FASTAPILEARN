from fastapi import APIRouter,HTTPException,status
from typing import List
from schema import BookModel,BookUpdate
from book_data import books
book_router = APIRouter()

book_router.get('/', status_code=200, response_model=List[BookModel])
async def get_books():
    return books


book_router.post('/createbook', status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookModel) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


book_router.get("/{book_id}")
async def get_book(book_id: int):
    for book in books:
        if book_id == book['id']:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Book not found'
    )


book_router.delete('/{book_id}', status_code=status.HTTP_200_OK)
async def delete_book(book_id: int):
    for book in books:
        if book_id == book['id']:
            books.remove(book)
            return {'message': 'Book deleted successfully'}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Book not found'
    )


book_router.patch('/updateBook/{book_id}')
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