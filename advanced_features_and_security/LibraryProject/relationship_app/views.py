from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library, Book
from .forms import BookForm  # type: ignore
from relationship_app.models import Book, Library  # type: ignore

def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@user_passes_test(lambda user: is_in_group(user, 'Viewers') or is_in_group(user, 'Editors') or is_in_group(user, 'Admins'), login_url='no_permission')
def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

@user_passes_test(lambda user: is_in_group(user, 'Editors') or is_in_group(user, 'Admins'), login_url='no_permission')
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@user_passes_test(lambda user: is_in_group(user, 'Editors') or is_in_group(user, 'Admins'), login_url='no_permission')
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

@user_passes_test(lambda user: is_in_group(user, 'Admins'), login_url='no_permission')
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})

def no_permission(request):
    return render(request, 'relationship_app/no_permission.html')
