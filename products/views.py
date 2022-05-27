from django.http import JsonResponse
from django.views import View

from .models import Product, Theme

# product 
class ProductThemeView(View):
    def get(self, request):
        theme = request.GET.get('theme', 'id')
        sort = request.GET.get('sort', 'id')

        sort_type= {
            "id"     : "id",
            "신메뉴순" : "-id",
            "높은가격순": "-price",
            "낮은가격순": "price"
        }

        themes = Theme.objects.get(theme=theme).id
        products = Product.objects.filter(producttheme__theme_id = themes).order_by(sort_type[sort])
        product_list = [{
            "id"      : product.id,
            "name"    : product.name,
            "serving" : product.serving,
            "cookTime": product.cook_time,
            "prepTime": product.prep_time,
            "price"   : product.price,
            # "image"   : image,
        } for product in products]
        return JsonResponse({'product_list': product_list, 'message': 'SUCCESS'}, status=200)