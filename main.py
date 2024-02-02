from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    isbn: int
    title: str
    description: str

my_books = [
    {"isbn":1, "title" : "BOOK1", "description": "Good"},
    {"isbn":2, "title" : "BOOK2", "description": "Bad"}
]

@app.get("/")
def get_all_books():
    return {"data": my_books}

def find_dict(isbn):
    for i,p in enumerate(my_books):
        if p["isbn"] == isbn:
            return i

def find_isbn(isbn: int):
    for i in my_books:
        if i['isbn'] == isbn:
            return i

@app.get("/book/{isbn}")
def get_book_by_isbn(isbn:int):
    my_dict = find_isbn(isbn)
    if not my_dict:
        raise Response(status.HTTP_404_NOT_FOUND)
    return {"data": my_dict}

@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    my_dict = book.model_dump()
    my_books.append(my_dict)
    return {"data":my_books}

@app.put("/book/{isbn}")
def update_book(isbn:int, book: Book):
    idx = find_dict(isbn)
    if idx == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"book with isbn {isbn} does not exist")
    my_dict = book.model_dump()
    my_dict["isbn"] = isbn
    my_books[idx] = my_dict
    return {"data": my_dict}

@app.delete("/book/{isbn}",status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_isbn(isbn:int):
    idx = find_dict(isbn)
    if idx == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"book with isbn {isbn} does not exist")
    my_books.pop(idx)
    
