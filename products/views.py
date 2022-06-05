from django.http import JsonResponse
from django.views import View

from .models import Product


class ProductListView(View):
    def get(self, request):
        try:
            sort   = request.GET.get('sort', '-id')
            
            filter_set = {
                "theme_id": "producttheme__theme_id",
                "search"  : "name__contains",
                "is_new"  : "is_new"
            }
            filter = {
                filter_set[key] : value for key, value in request.GET.items() if filter_set.get(key)
                }

            products = Product.objects.filter(**filter).order_by(sort)
            product_list = [{
                "id"      : product.id,
                "name"    : product.name,
                "serving" : product.serving,
                "cookTime": product.cook_time,
                "price"   : int(product.price),
                "spice"   : [spice.level for spice in product.spice_set.all()],
                "image"   : product.thumnail_image
            } for product in products]
            return JsonResponse({'product_list': product_list}, status=200)

        except KeyError:
            return JsonResponse({"message": 'KeyError'}, status = 400)  

class ProductDetailView(View):
    def get(self, request, id):
        try:
            products = Product.objects.get(id = id)
            product_detail = {
                "id"         : products.id,
                "name"       : products.name,
                "description": products.description,
                "serving"    : products.serving,
                "cookTime"   : products.cook_time,
                "prepTime"   : products.prep_time,
                "price"      : int(products.price),
                "spice"      : [spice.level for spice in products.spice_set.all()],
                "image"      : [image.image for image in products.productimage_set.all()]
            }
            return JsonResponse({'product_detail': product_detail}, status=200)

        except KeyError:
            return JsonResponse({"message": 'KeyError'}, status = 400)  
        except Product.DoesNotExist:
                return JsonResponse({"message": 'Not Found Data'}, status = 400)  