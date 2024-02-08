# Generated by Django 5.0.1 on 2024-02-08 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_reviewmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.bookmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='ReviewModel',
        ),
    ]
