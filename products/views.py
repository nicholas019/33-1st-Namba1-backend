from django.http import JsonResponse
from django.views import View

from .models import Product, ProductImage

# product 
class ProductThemeView(View):
    def get(self, request):
        theme = request.GET.get('theme')  # 

        products = Product.objects.filter(theme=theme)
        image = ProductImage.objects.filter(product_id = products.id)
        product_list = [{
                    "id"      : product.id,
                    "name"    : product.name,
                    "serving" : product.serving,
                    "cookTime": product.cook_time,
                    "prepTime": product.prep_time,
                    "price"   : product.price,
                    "image"   : image,
                } for product in products]
        
        return JsonResponse({'posting': product_list, 'message': 'SUCCESS'}, status=200)