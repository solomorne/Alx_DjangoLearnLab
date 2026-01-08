<!-- Create -->
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output:
# <Book: 1984>

<!-- Retrieve -->
from bookshelf.models import Book

# Retrieve the book created
t = Book.objects.get(title="1984")

# Display attributes
print(t.title, t.author, t.publication_year)

# Expected Output:
# 1984 George Orwell 1949

<!-- Update -->
from bookshelf.models import Book

# Fetch the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# Verify update
print(book.title)

# Expected Output:
# Nineteen Eighty-Four

<!-- Delete -->
from bookshelf.models import Book

# Fetch the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion by trying to retrieve all books
books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet []>