from django.shortcuts import render

# Create your views here.
from .models import Library
from django.http import HttpResponse
from relationship_app.models import Book, Library # type: ignore

def book_list(request):
    books = Book.objects.all()
    context = {'book_list': books}  
    return render(request, 'relationship_app/list_books.html', context)

from django.views.generic.detail import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all() 
        return context

    