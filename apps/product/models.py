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
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = models.TextField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
