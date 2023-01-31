from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('rate_product/<int:pk>', views.rate_product, name='rate_product'),
	path('product/<int:pk>', views.product_detail, name='product_detail'),
    
]