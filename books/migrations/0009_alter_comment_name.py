# Generated by Django 5.0.1 on 2024-02-08 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_comment_delete_reviewmodel'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.useraccount'),
        ),
    ]
