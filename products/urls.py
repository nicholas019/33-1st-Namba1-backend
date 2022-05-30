from django.urls import path

from products.views import ProductListView, ProductDetailView, MainProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/<int:id>', ProductDetailView.as_view()),
    path('/pc', MainProductListView.as_view()),
]
