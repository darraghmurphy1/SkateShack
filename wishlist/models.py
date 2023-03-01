from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist', default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} has been added to {self.user}'s wishlist"