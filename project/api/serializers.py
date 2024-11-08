from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Allows converting complex data into native Python datatypes.
    """
    class Meta:
        """
        Class to specify the model to be serialized and the fields to include.
        """
        model = Book
        fields = '__all__'