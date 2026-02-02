## Book API Views

- BookListView: Public read-only list of all books
- BookDetailView: Public read-only access to a single book
- BookCreateView: Authenticated users can create books
- BookUpdateView: Authenticated users can update books
- BookDeleteView: Authenticated users can delete books

Custom validation is enforced at the serializer level.
Permissions are handled using DRF's built-in permission classes.

## Advanced Querying for Books

The BookListView supports filtering, searching, and ordering.

### Filtering
/api/books/?publication_year=1960

### Search
/api/books/?search=achebe

### Ordering
/api/books/?ordering=-publication_year

Multiple query parameters can be combined.
