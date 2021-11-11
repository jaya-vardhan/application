from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    weight=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    created_at=models.CharField(max_length=100)
    updated_at=models.CharField(max_length=100)

    def __str__(self):
        return self.name

