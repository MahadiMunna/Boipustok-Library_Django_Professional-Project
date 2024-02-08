# Generated by Django 5.0.1 on 2024-02-08 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_bookborrowermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookmodel')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookborrowermodel')),
            ],
        ),
    ]
