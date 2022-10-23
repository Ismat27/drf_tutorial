from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15, default=99.99)

    def __str__(self):
        return f'{self.title}'

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "%.2f" %(float(self.price) * 0.2)