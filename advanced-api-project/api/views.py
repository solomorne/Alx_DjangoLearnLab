from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer


# ----------------------------
# LIST VIEW
# ----------------------------
# Read-only access for unauthenticated users
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ----------------------------
# DETAIL VIEW
# ----------------------------
# Read-only access for unauthenticated users
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ----------------------------
# CREATE VIEW
# ----------------------------
# Only authenticated users can create books
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ----------------------------
# UPDATE VIEW
# ----------------------------
# Only authenticated users can update books
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ----------------------------
# DELETE VIEW
# ----------------------------
# Only authenticated users can delete books
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Enable filtering, search, and ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    # Filtering by model fields
    filterset_fields = [
        'publication_year',
        'author',
        'title',
    ]

    # Search by text fields
    search_fields = [
        'title',
        'author__name',
    ]

    # Ordering options
    ordering_fields = [
        'title',
        'publication_year',
    ]

    # Default ordering
    ordering = ['title']