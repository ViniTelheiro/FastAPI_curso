from pydantic import Field, BaseModel
from typing import Optional



class Book():
    def __init__(self, id:int, title:str, author:str, description:str, rating:int) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    class Config:
        schema_extra = {
            'example':{
                'title': 'A new Title',
                'author': 'Random Person',
                'description': 'A new description of a book',
                'rating': 5

            }
        }


def set_book_id(book:Book, book_list:list):
    book.id = 1 if len(book_list) == 0 else book_list[-1].id + 1
    return book