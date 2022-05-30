from django.urls import path

from products.views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view()),
]
