from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware

from app.models import Book
from app.lib.function import get_books, post_books, get_book_detail, delete_book

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/books")
def api_get_books():
    return get_books()


@app.post("/books")
def api_post_books(book: Book):
    book_res = post_books(book)
    if book_res is not None:
        return Response(status_code=400)
    return Response(status_code=200)


@app.get("/books/book", response_model=Book)
def api_get_book_detail(title: str):
    return get_book_detail(title)


@app.delete("/book_delete")
def api_delete_book(title: str):
    book = delete_book(title)
    if book is not None:
        return Response(status_code=400)
    return Response(status_code=200)
