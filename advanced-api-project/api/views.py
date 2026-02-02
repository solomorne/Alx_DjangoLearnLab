from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ----------------------------
# LIST VIEW
# ----------------------------
# Allows anyone (authenticated or not) to retrieve all books.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------
# DETAIL VIEW
# ----------------------------
# Allows anyone to retrieve a single book by ID.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------
# CREATE VIEW
# ----------------------------
# Only authenticated users can create new books.
# Validation is handled automatically by BookSerializer.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# UPDATE VIEW
# ----------------------------
# Only authenticated users can update existing books.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# DELETE VIEW
# ----------------------------
# Only authenticated users can delete books.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
