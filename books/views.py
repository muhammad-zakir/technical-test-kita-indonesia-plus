from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from books.models import Books
from books.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Books.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(
        detail=False, permission_classes=[permissions.AllowAny], \
        description='API endpoint that allows books to be publicly viewed.'
    ) 
    def public(self, request):
        queryset = Books.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(
        detail=True, permission_classes=[permissions.AllowAny], \
        description='API endpoint that allows a book to be publicly viewed.', \
        url_path='public'
    )
    def public_detail(self, request, pk=None):
        queryset = Books.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
