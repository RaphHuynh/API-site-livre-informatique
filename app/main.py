from fastapi import FastAPI, Response

from app.models import Book
from app.lib.function import get_books, post_books, get_book_detail

app = FastAPI()


@app.get("/books")
def api_get_books():
    return get_books()


@app.post("/books")
def api_post_books(book: Book):
    book_res = post_books(book)
    if book_res is not None:
        return Response(status_code=400)
    return Response(status_code=201)


@app.get("/books/book", response_model=Book)
def api_get_book_detail(title: str):
    return get_book_detail(title)
