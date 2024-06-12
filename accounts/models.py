from django.db import models

# Create your models here.
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('purchase', 'Purchase'), ('payment', 'Payment')])
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.transaction_type == 'purchase':
            self.account.balance -= self.amount
        elif self.transaction_type == 'payment':
            self.account.balance += self.amount
        self.account.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.account.name} - {self.transaction_type} - {self.amount}"
