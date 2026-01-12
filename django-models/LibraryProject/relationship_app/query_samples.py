import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    # This uses the filter method on Book
    books = Book.objects.filter(author=author)
    return books

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    # This retrieves all books associated with the ManyToMany field
    return library.books.all()

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    # This meets your specific requirement: Librarian.objects.get(library=...)
    librarian = Librarian.objects.get(library=library)
    return librarian

if __name__ == "__main__":
    # Example usage (ensure these records exist in your DB first)
    print("Query script ready.")