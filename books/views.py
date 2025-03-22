import datetime
from books.models import Books, BorrowedBooks
from books.serializers import BookSerializer, BorrowedBookSerializer
from library.serializers import UserIdentifierSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Books.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(
        description='API endpoint that allows books to be publicly viewed.',
        detail=False,
        permission_classes=[permissions.AllowAny]
    )
    def public(self, request):
        queryset = Books.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(
        description='API endpoint that allows a book to be publicly viewed.',
        detail=True,
        permission_classes=[permissions.AllowAny],
        url_path='public'
    )
    def public_detail(self, request, pk=None):
        queryset = Books.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class BorrowedBookViewSet(ModelViewSet):
    """
    API endpoint that allows borrowed books to be viewed or edited.
    """
    queryset = BorrowedBooks.objects.all().order_by('-created_at')
    serializer_class = BorrowedBookSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(
        description='API endpoint that allows a book to be borrowed.',
        detail=False,
        permission_classes=[permissions.IsAuthenticated],
        methods=['post']
    )
    def borrow(self, request,):
        book_id = request.data['book_id']

        if not book_id:
            return Response(
                {'error': 'The book_id field is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        book = get_object_or_404(Books, id=book_id)

        borrowed_book = BorrowedBooks.objects.filter(
            book_id=book_id,
            returned_at__isnull=True
        )

        if borrowed_book:
            return Response(
                {'error': 'Sorry, the selected book is already borrowed'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_serializer = UserIdentifierSerializer(request.user)

        borrowed_book = BorrowedBooks(
            book_id=book_id, 
            user_id=user_serializer.data['id']
        )
        borrowed_book.save()

        serializer = BorrowedBookSerializer(borrowed_book)

        return Response(serializer.data)

    @action(
        description='API endpoint that allows a book to be returned.',
        detail=False,
        permission_classes=[permissions.IsAuthenticated],
        methods=['post'],
        url_path='return'
    )
    def return_book(self, request):
        borrow_id = request.data['borrow_id']

        if not borrow_id:
            return Response(
                {'error': 'The borrow_id field is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        borrowed_book = get_object_or_404(BorrowedBooks, id=borrow_id)

        if not borrowed_book:
            return Response(
                {'error': 'Sorry, you have not yet borrowed the selected book'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if borrowed_book.returned_at:
            return Response(
                {'error': 'Sorry, you have returned the borrowed book'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_serializer = UserIdentifierSerializer(request.user)
        if borrowed_book.user_id != user_serializer.data['id']:
            return Response(
                {'error': 'Sorry, you are not the one borrowing this book'},
                status=status.HTTP_400_BAD_REQUEST
            )

        borrowed_book.returned_at = datetime.datetime.now()
        borrowed_book.save()

        serializer = BorrowedBookSerializer(borrowed_book)

        return Response(serializer.data)