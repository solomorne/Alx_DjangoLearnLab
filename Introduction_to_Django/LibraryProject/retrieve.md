from bookshelf.models import Book

# Retrieve the book created
t = Book.objects.get(title="1984")

# Display attributes
print(t.title, t.author, t.publication_year)

# Expected Output:
# 1984 George Orwell 1949