## Book API Views

- BookListView: Public read-only list of all books
- BookDetailView: Public read-only access to a single book
- BookCreateView: Authenticated users can create books
- BookUpdateView: Authenticated users can update books
- BookDeleteView: Authenticated users can delete books

Custom validation is enforced at the serializer level.
Permissions are handled using DRF's built-in permission classes.
