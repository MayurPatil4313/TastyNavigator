
from django.contrib import admin
from django.urls import include, path
from home_app.views import views

from recommendation import views as vs
from recommendation.views import add_to_cart
urlpatterns = [
    path("",views.index, name='Home'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("login",views.login, name='login'),
    path("Registration",views.Registration, name='Registration'),
    path("handlesignin",views.handlesignin, name='handlesignin'),
    path("logout",views.handlelogout, name='handlelogout'),
    path("handlecontact",views.handlecontact, name='handlecontact'),
    path("Veg_categories",views.Veg_categories, name='Veg_categories'),
    path("Non_Veg_categories",views.Non_Veg_categories, name='Non_Veg_categories'),
    path("seafood_categories",views.seafood_categories, name='seafood_categories'),
    path("beverage_categories",views.beverage_categories, name='beverage_categories'),
    path("dessert_categories",views.dessert_categories, name='dessert_categories'),
    path("vegan_categories",views.vegan_categories, name='vegan_categories'),
    path("breakfast_categories",views.breakfast_categories, name='breakfast_categories'),

    path('handleOrder/', views.handle_order, name='handle_order'),
    path('userorder/', views.userorder, name='userorder'),
    path('ThankYou/', views.ThankYou, name='ThankYou'),



    path("birini",views.birini, name='birini'),
    path("cake",views.cake, name='cake'),
    path("paneer",views.paneer, name='paneer'),
    path("virgin",views.virgin, name='virgin'),
    path("haka",views.haka, name='haka'),
    path("pasta",views.pasta, name='pasta'),









    path('recommendation/add_to_cart/<int:dish_id>/', add_to_cart, name='add_to_cart'),





    #path("filter",views.filter, name='filter'),

    path("recommendation",vs.recommendation, name='recommendation'),



]
