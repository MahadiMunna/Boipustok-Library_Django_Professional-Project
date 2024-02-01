from django.contrib import admin
from .models import BookModel, BookCategory

# Register your models here.
admin.site.register(BookModel)
admin.site.register(BookCategory)