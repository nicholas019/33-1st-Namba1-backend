
from itertools import product
import json
from django.views import View


class Cart(View):
    def post(self, request):
        cart_data = json.loads(request.body)

        quantity = cart_data["quntity"]
        product_id = cart_data["product_id"]
        user_id = request.user
        
        cart =