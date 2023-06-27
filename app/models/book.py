import dataclasses

from pydantic import BaseModel
from datetime import datetime


class BookSummary(BaseModel):
    title: str
    author: str
    image: str


class Book(BookSummary):
    isbn: str
    description: str
    edition: str
    date: datetime
