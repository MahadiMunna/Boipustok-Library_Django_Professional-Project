from django.contrib import admin
from .models import BookModel, BookCategory

# Register your models here.
admin.site.register(BookModel)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ['category_name','slug']

admin.site.register(BookCategory, CategoryAdmin)