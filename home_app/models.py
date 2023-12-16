from django.db import models

class Registration_Data(models.Model):

    name = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
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



# MyModel.objects.create(card_number=card_number, expiration_date=expiration_date, cvv_code=cvv_code, card_holder_name=card_holder_name)


class Order(models.Model):
    card_number = models.CharField(max_length=17)
    expiration_date = models.CharField(max_length=50)
    cvv_code = models.CharField(max_length=10)
    card_holder_name = models.CharField(max_length=25)

    amount = models.CharField(max_length=25)

    def __str__(self):
        return self.card_holder_name







