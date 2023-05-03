from django.db import models

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order_number}"