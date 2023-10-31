from django.db import models
from apps.account.models import Account


class Place(models.Model):
    name = models.CharField(max_length=221)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=221)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=221)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Storehouse(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account}'s product - {self.product}"
