from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering,
    and permission enforcement.
    """

    def setUp(self):
        """
        Set up test data before each test runs.
        """
        # Create user for authenticated requests
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create author
        self.author = Author.objects.create(name="Chinua Achebe")

        # Create books
        self.book1 = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="No Longer at Ease",
            publication_year=1960,
            author=self.author
        )

        # URLs
        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book1.id}/"
        self.delete_url = f"/api/books/delete/{self.book1.id}/"

    # ----------------------------
    # READ TESTS
    # ----------------------------
    def test_list_books_public_access(self):
        """
        Unauthenticated users should be able to list books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_books_with_filtering(self):
        """
        Test filtering books by publication_year.
        """
        response = self.client.get(
            self.list_url,
            {"publication_year": 1958}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Things Fall Apart")

    def test_search_books_by_title(self):
        """
        Test search functionality using title.
        """
        response = self.client.get(
            self.list_url,
            {"search": "Fall"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication_year.
        """
        response = self.client.get(
            self.list_url,
            {"ordering": "-publication_year"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data[0]["publication_year"],
            1960
        )

    # ----------------------------
    # CREATE TESTS
    # ----------------------------
    def test_create_book_unauthenticated(self):
        """
        Unauthenticated users should NOT be able to create books.
        """
        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """
        Authenticated users should be able to create books.
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ----------------------------
    # UPDATE TESTS
    # ----------------------------
    def test_update_book_authenticated(self):
        """
        Authenticated users should be able to update books.
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Things Fall Apart (Updated)",
            "publication_year": 1958,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Things Fall Apart (Updated)")

    # ----------------------------
    # DELETE TESTS
    # ----------------------------
    def test_delete_book_unauthenticated(self):
        """
        Unauthenticated users should NOT be able to delete books.
        """
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        """
        Authenticated users should be able to delete books.
        """
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
