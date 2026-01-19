from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# Create your views here.
# Enforcing permissions in views
@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    # Logic to add a book
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic to edit the book
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic to delete the book
    book.delete()
    return redirect('book_list')


def book_list(request):
    # Step 3: Preventing SQL Injection using Django ORM
    # The ORM handles parameterization automatically
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def search_books(request):
    # Validating user input through forms prevents malicious data entry
    form = ExampleForm(request.GET)
    books = []
    if form.is_valid():
        title = form.cleaned_data['book_title']
        # Secure: Django parameterizes this query
        books = Book.objects.filter(title__icontains=title)
    
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})