# FastAPI Book Management

This repository contains my implementation of a basic CRUD API for managing a collection of books using FastAPI in Python. It showcases my understanding and progress in building web APIs with FastAPI.

## Features

- CRUD operations (Create, Read, Update, Delete) for managing books.
- Proper error handling and validation for incoming requests.
- Endpoints to:
  - Get a list of all books
  - Get details of a specific book by its ISBN
  - Add a new book
  - Update details of an existing book by its ISBN
  - Delete a book by its ISBN

## Setup Instructions


```bash
git clone https://github.com/neerajjez/FastAPI-Book-Management.git
cd FastAPI-Book-Management
pip install -r requirements.txt
uvicorn main:app --reload

