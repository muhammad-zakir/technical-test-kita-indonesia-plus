from django.conf import settings
from django.db import models


class Books (models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


    class Meta:
        db_table = 'books'
        ordering = ['-created_at']


class BorrowedBooks (models.Model):
    returned_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    book = models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    class Meta:
        db_table = 'borrowed_books'
        ordering = ['-created_at']