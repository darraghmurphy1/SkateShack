from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_wishlist, name='wishlist'),
    path('add_wishlist/<int:product_id>/', views.add_wishlist, name='wishlist_add'),
    path('delete_wishlist/<int:wishlist_id>/', views.delete_wishlist, name='delete_wishlist'),
]
