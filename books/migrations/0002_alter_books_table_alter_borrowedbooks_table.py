# Generated by Django 5.1.7 on 2025-03-21 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='books',
            table='books',
        ),
        migrations.AlterModelTable(
            name='borrowedbooks',
            table='borrowed_books',
        ),
    ]
