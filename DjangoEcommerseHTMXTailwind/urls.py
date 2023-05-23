
from django.contrib import admin
from django.urls import path

from core.views import frontpage, shop
from product.views import product
from cart.views import add_to_cart

urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('shop/', shop, name='shop'),
    path('admin/', admin.site.urls),
    path('shop/<slug:slug>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart')
]
