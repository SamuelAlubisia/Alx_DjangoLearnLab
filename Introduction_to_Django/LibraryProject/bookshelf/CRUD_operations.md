# CRUD Operations in Django Shell

## **1. Create a Book**
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Output 
<Book: 1984 by George Orwell (1949)>

#Retrive book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

#Output
1984 George Orwell 1949

#Update book
book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id).title)

#Output
Nineteen Eighty-Four

#Delete book
book.delete()
print(Book.objects.all())  # Should be empty if no other books exist

#Output
(1, {'bookshelf.Book': 1})
<QuerySet []>
