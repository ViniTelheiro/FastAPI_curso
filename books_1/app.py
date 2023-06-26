from fastapi import FastAPI, Body

BOOKS = [
    {"title": "Title One", "author": "Author One", "category":"science"},
    {"title": "Title Two", "author": "Author Two", "category":"science"},
    {"title": "Title Three", "author": "Author Three", "category":"history"},
    {"title": "Title Four", "author": "Author Four", "category":"math"},
    {"title": "Title Five", "author": "Author Five", "category":"math"},
    {"title": "Title Six", "author": "Author Two", "category":"math"}
]


app = FastAPI()

############ GET Request method ############

@app.get("/books/all")
async def get_all_books():
    return BOOKS

#Query parameters
@app.get("/books/")
async def get_book_by_category(category:str):
    books_to_return = list(filter(lambda x:x.get('category').casefold() == category.casefold(), BOOKS))
    return books_to_return

#Dynamic parameter:
@app.get("/books/{book_title}")
async def get_single_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

#Dynamic with query parameters:
@app.get("/book/{book_author}/")
async def get_category_by_author(book_author:str, category:str):
    books_to_return = list(filter(lambda x:x.get('author').casefold() == book_author.casefold() and x.get('category').casefold() == category.casefold(), BOOKS))
    return books_to_return

############ POST Request method ############

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

############ PUT Request method ############

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i, book in enumerate(BOOKS):
        if book.get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

############ DELETE Request method ############

@app.delete("/books/delete_books/{book_title}")
async def delete_book(book_title:str):
    for i, book in enumerate(BOOKS):
        if book.get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)