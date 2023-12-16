from django.contrib import admin

# Register your models here.
from recommendation.models import Menu, Contacts , CartItem

admin.site.register(Menu)
admin.site.register(Contacts)
admin.site.register(CartItem)
