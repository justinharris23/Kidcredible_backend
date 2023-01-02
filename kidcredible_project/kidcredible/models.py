from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, default='no name')
    type = models.CharField(max_length=50, default='no type')
    description = models.CharField(max_length=250, default='no description')
    image = models.CharField(max_length=50, default='no image')
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews', null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews', null=True)
    name = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    body = models.CharField(max_length=250, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)

    def __str__(self):
        return self.name
