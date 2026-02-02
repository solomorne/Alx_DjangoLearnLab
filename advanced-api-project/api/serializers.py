from rest_framework import serializers
from datetime import date
from .models import Author, Book


# BookSerializer handles serialization and validation for Book objects.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to prevent future publication years
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# AuthorSerializer serializes Author data and includes nested books.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to dynamically include related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
