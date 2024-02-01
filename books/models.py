from django.db import models

# Create your models here.
class BookCategory(models.Model):
    category_name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.category_name
    
class BookModel(models.Model):
    book_title = models.CharField(max_length=200)
    book_description = models.TextField()
    book_category = models.ManyToManyField(BookCategory)
    book_image = models.ImageField(upload_to='./books/uploads/', blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return self.book_title

