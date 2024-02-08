from django.db import models
from users.models import UserAccount

# Create your models here.

class Transaction(models.Model):
    account = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits = 12,null = True)
    transaction_type = models.CharField(max_length=10, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
    
    def __str__(self):
        return f"{self.transaction_type} - {self.account.user.first_name}"
