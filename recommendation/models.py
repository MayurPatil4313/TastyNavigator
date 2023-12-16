from django.db import models
# models.py
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Menu(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    dish_name = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    user_rating = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    cuisine = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


    def __str__(self):
        return self.dish_name








class Contacts(models.Model):

    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name








# modified my self


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish_id = models.IntegerField()
    dish_name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    calories = models.IntegerField()
    cuisine = models.CharField(max_length=255)
    user_rating = models.FloatField()
    category = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)  # Add this line for quantity

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return "{}'s {}".format(self.user.username, self.dish_name)





