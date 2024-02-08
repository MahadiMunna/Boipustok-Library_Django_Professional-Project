from django.contrib import admin
from .models import BookModel, BookCategory, BookBorrowerModel

# Register your models here.
admin.site.register(BookModel)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ['category_name','slug']

admin.site.register(BookCategory, CategoryAdmin)
@admin.register(BookBorrowerModel)
class BookBorrowerModelAdmin(admin.ModelAdmin):
    list_display = ['borrower', 'book', 'transaction']
    
    def save_model(self, request, obj, change):
        obj.borrower = obj.borrower
        obj.book = obj.book
        obj.transaction = obj.transaction
        obj.borrower.save()
        super().save_model(request, obj, change)