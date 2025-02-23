# Command:
```python
from bookshelf.models import Book

# Creating a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Print the ID of the created book to confirm successful creation
print(book.id)
