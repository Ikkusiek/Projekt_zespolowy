from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    quantity = models.DecimalField(max_digits=4, decimal_places=0, validators=[MinValueValidator(Decimal('0'))])
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name
