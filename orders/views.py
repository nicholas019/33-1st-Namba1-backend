import json

from django.http import JsonResponse
from django.views import View

from core.utils import token_reader
from products.models import ProductImage
from .models import Cart


class CartView(View):
    @token_reader
    def post(self, request):
        try:
            cart_data = json.loads(request.body)

            quantity   = cart_data["quantity"]
            product_id = cart_data["product_id"]
            user_id    = request.user
            
            Cart.objects.create(quantity   = quantity, 
                                product_id = product_id,
                                user_id    = user_id
                                )
            return JsonResponse({'message':'SUCCES'}, status=200)
        except KeyError:
            return JsonResponse({"message": 'KEY_ERROR'}, status = 400)   
        except TypeError:
            return JsonResponse({"message": '이미 장바구니에 담겨있습니다'}, status = 400)    

    @token_reader
    def get(self, request):
        try:
            carts = Cart.objects.filter(user_id = request.user)
            
            cart_list=[{
                "user_id"      : cart.user_id,
                "product_name" : cart.product.name,
                "product_price": int(cart.product.price),
                "product_image": ProductImage.objects.filter(product_id=cart.product_id)[2].image,
                "quantity"     : cart.quantity,
            } for cart in carts]

            return JsonResponse({ "cart":cart_list, "message":"SUCCESS"}, status=200) 
        except KeyError:
            return JsonResponse({"message": 'KEY_ERROR'}, status = 400)    

    @token_reader
    def patch(self, request):
        try:
            cart_data = json.loads(request.body)

            quantity   = cart_data["quantity"]
            product_id = cart_data["product_id"]
            user_id    = request.user

            cart = Cart.objects.get(user_id = user_id, product_id = product_id)
            cart.quantity = quantity
            cart.save()

            return JsonResponse({"message":"UPDATE SUCCESS"}, status=200) 
        except KeyError:
            return JsonResponse({"message": 'KEY_ERROR'}, status = 400)
        except Cart.DoesNotExist:
            return JsonResponse({"message": 'Not found Data'}, status = 400)    


    def delete(self, request):
        try:    
            cart_delete= request.GET.get('delete', None)
            
            cart = Cart.objects.get(id = cart_delete)
            cart.delete()

            return JsonResponse({"message":"DELETE SUCCESS"}, status=200) 
        except Cart.DoesNotExist:
            return JsonResponse({"message": 'Not found Data'}, status = 400)    