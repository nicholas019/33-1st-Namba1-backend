from django.http import JsonResponse
from django.views import View

from .models import Product, Theme


class ProductListView(View):
    def get(self, request):
        theme = request.GET.get('theme', "KIDS")
        sort = request.GET.get('sort', "신메뉴순")

        sort_type= {
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
            "spice"   : [spice.level for spice in product.spice_set.all()],
            "image"   : [image.image for image in product.productimage_set.all()][0]
        } for product in products]
        return JsonResponse({'product_list': product_list, 'message': 'SUCCESS'}, status=200)