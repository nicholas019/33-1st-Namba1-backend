from django.http import JsonResponse
from django.views import View

from .models import Product

class ProductView(View):
    def get(request):
        products = Product.objects.filter(theme=request.theme)
        product_list = [{
                    'id'         : product.id,
                    'name'      : product.title,
                    'serving'    : product.content,
                    'cookTime'  : product.image_url,
                    'price'  : product.image_url,
                } for product in products]
        
        return JsonResponse({'posting': product_list, 'message': 'SUCCESS'}, status=200)