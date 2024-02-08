from django.db import models
from users.models import UserAccount
from transactions.models import Transaction

# Create your models here.
class BookCategory(models.Model):
    category_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    
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

class BookBorrowerModel(models.Model):
    borrower = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.book.book_title} borrow by {self.borrower.user.first_name}"


