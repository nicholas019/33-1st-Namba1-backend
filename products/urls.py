from django.urls import path

from products.views import ProductThemeView

urlpatterns = [
    path('/theme', ProductThemeView.as_view()),
]
