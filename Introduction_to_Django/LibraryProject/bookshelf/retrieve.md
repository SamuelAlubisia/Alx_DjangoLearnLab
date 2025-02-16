# Retrieve All Books

## Command:
```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()

# Display each book's details
for book in books:
    print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

books = Book.objects.all()
print(books)