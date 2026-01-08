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