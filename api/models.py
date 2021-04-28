from typing import Optional, List
from pydantic import BaseModel

from datetime import date


class Author(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    author: Author
    release_date: str
