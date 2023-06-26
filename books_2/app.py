from fastapi import FastAPI, Path, Query, HTTPException
from utils import Book, BookRequest, set_book_id


BOOKS = [
    Book(1, 'Computer Science Pro', 'Author One', 'A very nice book', 5),
    Book(2, 'Be Fast with FastAPI', 'Author One', 'A great book', 5),
    Book(3, 'Master Endpoints', 'Author One', 'A awesome book', 5),
    Book(4, 'HP1', 'Author Two', 'Random description 1', 2),
    Book(5, 'HP2', 'Author Three', 'Random description 2', 3),
    Book(6, 'HP3', 'Author Four', 'A very random description', 1)
]

app = FastAPI()

@app.get("/books")
async def get_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/")
async def get_book_by_rating(book_rating:int=Query(gt=0, lt=6)):
    returned_books = list(filter(lambda x:x.rating==book_rating, BOOKS))
    return returned_books

@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(set_book_id(new_book, BOOKS))

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    update = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            update = True
    if not update:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.delete("/books/delete/{book_id}")
async def delete_book(book_id:int=Path(gt=0)):
    delete = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
    if not delete:
       raise HTTPException(status_code=404, detail="Item not found")




