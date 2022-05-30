from django.urls import path, include

urlpatterns = [
    path('user', include('users.urls')),
    path('products', include('products.urls')),
    path('main', include('products.urls')),
]
