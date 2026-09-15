from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    """Dados necessários para criar ou atualizar um livro."""

    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0, le=datetime.now().year)


books = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937},
    {"id": 2, "title": "Frankenstein", "author": "Mary Shelley", "year": 1818},
]


@app.get("/")
def read_root():
    """Retorne uma mensagem para confirmar que a API está funcionando."""
    pass


@app.get("/books")
def list_books():
    """Retorne todos os livros do catálogo."""
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Retorne um livro pelo identificador."""
    pass


@app.post("/books", status_code=201)
def create_book(book: BookCreate):
    """Crie um livro no catálogo."""
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    """Atualize um livro existente."""
    pass


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    """Remova um livro do catálogo."""
    pass
