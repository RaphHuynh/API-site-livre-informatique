import dataclasses
import json

from fastapi.encoders import jsonable_encoder
from unidecode import unidecode
from app.models import Book, BookSummary
import os


def get_books():
    path = "./app/bd"
    list_repository_books = os.listdir(path)
    dict_books = []
    for book in list_repository_books:
        with open(f"{path}/{book}/summary.json", "r") as book_summary:
            data_book = json.load(book_summary)
            dict_books.append(data_book)
    return dict_books


def post_books(book: Book):
    path = "./app/bd"
    name_repository_book = unidecode(book.title).strip()
    os.mkdir(f"{path}/{unidecode(book.title)}")
    try:
        with open(f"{path}/{name_repository_book}/summary.json", "w") as file_book_summary:
            new_book_summary = BookSummary(title=book.title, author=book.author, image=book.image)
            json.dump(jsonable_encoder(new_book_summary), file_book_summary, indent=3)
        file_book_summary.close()
        with open(f"{path}/{name_repository_book}/detail.json", "w") as file_book_detail:
            new_book_detail = Book(title=book.title,author=book.author,image=book.image, isbn=book.isbn, description=book.description, edition=book.edition, date=book.date)
            json.dump(jsonable_encoder(new_book_detail), file_book_detail, indent=7)
    except FileNotFoundError:
        return "File Error"
    return None


def get_book_detail(title: str):
    path = "./app/bd"
    name_repository_book = unidecode(title).strip()
    try:
        with open(f"{path}/{name_repository_book}/detail.json", "r") as file_book_detail:
            data_book = json.load(file_book_detail)
    except FileNotFoundError:
        return None
    return data_book
