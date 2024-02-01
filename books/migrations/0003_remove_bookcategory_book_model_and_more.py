# Generated by Django 4.2.9 on 2024-02-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_bookcategory_book_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcategory',
            name='book_model',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='book_category',
            field=models.ManyToManyField(to='books.bookcategory'),
        ),
    ]
