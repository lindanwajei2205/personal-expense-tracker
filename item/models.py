from django.db import models
from category.models import Category
from django.contrib.auth.models import User


class Item(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name