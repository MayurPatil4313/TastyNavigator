
from django.contrib import admin
from django.urls import include, path
from recommendation import views
from .views import add_to_cart, view_cart , update_cart_quantity , update_cart_item_quantity

urlpatterns = [
    path('recommendation',views.recommendation, name='recommendation'),
    path('filter',views.filter, name='filter'),
    path('Ingredients',views.Ingredients , name='Ingredients'),
    #path('recommendation',views.recommendation, name='recommendation'),

    path('add_to_cart/<int:dish_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),

    path('remove_from_cart/<int:dish_id>/', views.remove_from_cart, name='remove_from_cart'),
    path("order",views.order, name='order'),
    #path('update_cart_quantity/', update_cart_quantity, name='update_cart_quantity'),
    path('update_cart_item_quantity/<int:dish_id>/<int:new_quantity>/', update_cart_item_quantity,
         name='update_cart_item_quantity'),


]
