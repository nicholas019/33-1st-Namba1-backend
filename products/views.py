from django.http import JsonResponse
from django.views import View

from .models import Product, Theme


class ProductListView(View):
    def get(self, request):
        try:
            theme  = request.GET.get('theme', "KIDS")
            sort   = request.GET.get('sort', "신메뉴순")
            search = request.GET.get('search', None)


            sort_type= {
                "신메뉴순" : "-id",
                "높은가격순": "-price",
                "낮은가격순": "price"
            }
            if theme:    
                themes   = Theme.objects.get(theme=theme).id
                products = Product.objects.filter(producttheme__theme_id = themes).order_by(sort_type[sort])

            if search != None:
                products = Product.objects.filter(name__contains=search).order_by(sort_type[sort])

            product_list = [{
                "id"      : product.id,
                "name"    : product.name,
                "serving" : product.serving,
                "cookTime": product.cook_time,
                "price"   : int(product.price),
                "spice"   : [spice.level for spice in product.spice_set.all()],
                "image"   : [image.image for image in product.productimage_set.all()][0]
            } for product in products]
            return JsonResponse({'product_list': product_list, 'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({"message": 'KeyError'}, status = 400)  
        except Product.DoesNotExist:
            return JsonResponse({"message": 'No Data'}, status = 400)


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
            return JsonResponse({'product_detail': product_detail, 'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({"message": 'KeyError'}, status = 400)  
        except Product.DoesNotExist:
            return JsonResponse({"message": 'No Data'}, status = 400)

class MainProductListView(View):
    def get(self, request):
        try:
            theme = request.GET.get('theme', None)
            new   = request.GET.get('new', None)
            all   = request.GET.get('all', None)

            if theme:
                themes   = Theme.objects.get(theme=theme).id
                products = Product.objects.filter(producttheme__theme_id = themes).order_by('-id')
                i = 2

            if new:
                product  = Product.objects.all().order_by('-id')
                products = product[:5]
                i = 1

            if all:
                products = Product.objects.all().order_by('-id')
                i = 2

            product_list = [{
                    "id"      : product.id,
                    "name"    : product.name,
                    "serving" : product.serving,
                    "price"   : int(product.price),
                    "image"   : [image.image for image in product.productimage_set.all()][i]
                } for product in products]


            return JsonResponse({
                'product_list': product_list,
                'message'     : 'SUCCESS'
                }, status=200)   

        except KeyError:
            return JsonResponse({"message": 'KeyError'}, status = 400)    