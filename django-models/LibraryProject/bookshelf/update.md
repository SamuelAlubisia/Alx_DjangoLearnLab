# Update the Book's Title

## Command:
```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)
