# Generated by Django 5.1.7 on 2025-03-22 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_book_id_borrowedbooks_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='borrowedbooks',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
