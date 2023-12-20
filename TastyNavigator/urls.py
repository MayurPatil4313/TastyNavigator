"""
URL configuration for TastyNavigator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "Adminstration"
admin.site.site_title = "Adminstration Panel"
admin.site.index_title = "Welcome to TastyNavigation"
from recommendation import views
from recommendation.views import add_to_cart, view_cart ,remove_from_cart ,order , update_cart_quantity , update_cart_item_quantity , process_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_app.urls')),

    path('recommendation/',views.recommendation),

    path('filter/',views.filter),

path('Ingredients/',views.Ingredients),

    path('add_to_cart/<int:dish_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),

    path('remove_from_cart/<int:dish_id>/', views.remove_from_cart, name='remove_from_cart'),

    path("order/",views.order, name='order'),

    # path('update_cart_quantity/', update_cart_quantity, name='update_cart_quantity'),

    path('update_cart_item_quantity/<int:dish_id>/<int:new_quantity>/', update_cart_item_quantity,
         name='update_cart_item_quantity'),

    path('process_order/<str:payment_id>/<str:signature>/', process_order, name='process_order'),


]


