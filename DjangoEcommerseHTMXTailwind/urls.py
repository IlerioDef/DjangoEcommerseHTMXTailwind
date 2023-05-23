from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from core.views import frontpage, shop, signup
from product.views import product
from cart.views import add_to_cart, cart, checkout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('', frontpage, name="frontpage"),
    path('shop/', shop, name='shop'),
    path('admin/', admin.site.urls),
    path('shop/<slug:slug>/', product, name='product'),
    path('cart/', cart, name='cart'),
    path('cart/checkout/', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
