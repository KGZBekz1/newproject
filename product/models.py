from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')