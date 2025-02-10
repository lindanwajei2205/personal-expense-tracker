from django.db import models
from category.models import Category
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = "comments"
        verbose_name = "Comment"