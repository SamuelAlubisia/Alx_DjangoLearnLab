import os
import django

sys.path.append('/C:/Users/TOSHIBA/Alx_DjangoLearnLab/django-models/LibraryProject')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian # type: ignore
import sys

def get_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)
        print([book.title for book in books])
    else:
        print("Author not found.")

def get_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        books = library.books.all()
        print([book.title for book in books])
    else:
        print("Library not found.")

def get_librarian_for_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        librarian = Librarian.objects.filter(library=library).first()
        if librarian:
            print(librarian.name)
        else:
            print("Librarian not found.")
    else:
        print("Library not found.")
