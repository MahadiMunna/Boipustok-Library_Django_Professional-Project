# Generated by Django 4.2.9 on 2024-02-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_bookcategory_book_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='./books/uploads/'),
        ),
    ]
