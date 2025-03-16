from rest_framework import serializers # type: ignore
from . models import Author,Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' #Includes all fields
    def validate_validate_publication_year(self, value):
        """Ensure the publication year is not in the future"""
        current_year = datetime.now().year
        if value > current_year: #The value represents the user-inputted data for the publication_year field 
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value # Return valid value if no error


class AuthorSerializer(serializers.ModelSerializer):
    # Nested Serializer to include all books written by the author (One-to-Many relationship)
    books = BookSerializer(many=True, read_only=True) #read_only=True: This ensures books are only displayed in responses but not created directly through this serializer.
    class Meta:
        model = Author
        fields = ['name', 'books'] ## Includes author's name and their related books