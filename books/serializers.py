from books.models import Books, BorrowedBooks
from library.serializers import UserSerializer
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ['name']


class BorrowedBookSerializer(serializers.HyperlinkedModelSerializer):
    book = BookSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    book_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = BorrowedBooks
        fields = ['user_id', 'book_id', 'created_at', 'returned_at', 'book', 'user']
        read_only_fields = ['book', 'user']