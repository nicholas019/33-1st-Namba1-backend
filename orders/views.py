import json

from django.http import JsonResponse
from django.views import View

from core.utils import login_required
from .models import Cart


class CartView(View):
    @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)

            quantity   = data["quantity"]
            product_id = data["product_id"]
            user_id    = request.user.id
            
            cart, created = Cart.objects.get_or_create(
                product_id = product_id,
                user_id    = user_id,
                defaults   = {"quantity" : quantity}
                )
            if not created:
                cart.quantity += quantity
                cart.save()

            return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({"message": 'KEY_ERROR'}, status = 400)   

    @login_required
    def get(self, request):
        try:
            carts = Cart.objects.filter(user_id = request.user.id)
            
            cart_list=[{
                "user_id" : cart.user_id,
                "name"    : cart.product.name,
                "price"   : int(cart.product.price),
                "image"   : cart.thumnail_image,
                "quantity": cart.quantity,
            } for cart in carts]

            return JsonResponse({ "cart":cart_list}, status=200) 
            
        except KeyError:
            return JsonResponse({"message": 'KEY_ERROR'}, status = 400)    

    @login_required
    def patch(self, request, cart_id):
        try:
            cart_data = json.loads(request.body)

            quantity   = cart_data["quantity"]
            
            cart = Cart.objects.get(user_id = request.user.id, cart_id = cart_id)
            cart.quantity = quantity
            cart.save()

            return JsonResponse(status=200) 

        except KeyError:
            return JsonResponse({"message": 'KEY_ERROR'}, status = 400)
        except Cart.DoesNotExist:
            return JsonResponse({"message": 'Not found Data'}, status = 400)    

    @login_required
    def delete(self, request, cart_id):
        Cart.objects.filter(user_id = request.user.id, id = cart_id).delete()
        return JsonResponse({"message": 'SUCCESS'},status=200) 