from django.db import models
from django.contrib.auth.models import User
from recommendation.models import CartItem

from django.utils import timezone

class Registration_Data(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=15)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    security = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.name




class Contacts(models.Model):

    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name







from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Use the ID of a specific user
    card_number = models.CharField(max_length=17)
    expiration_date = models.CharField(max_length=50)
    cvv_code = models.CharField(max_length=10)
    card_holder_name = models.CharField(max_length=25)

    amount = models.CharField(max_length=25)

    # Add fields for dish information with default values
    dish_name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.PositiveIntegerField(default=1)

    # Add DateTimeField for storing date and time
    order_datetime = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Calculate the amount based on dish price and quantity
        self.amount = self.price * self.quantity
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.card_holder_name




