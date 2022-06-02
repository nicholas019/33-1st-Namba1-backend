import json
import datetime

from django.http import JsonResponse
from django.views import View

from core.utils import login_required
from .models import Review
from users.models import User

class ReviewView(View):
    # @login_required
    def post(self, request):
        try:
            data = json.loads(request.body)

            title      = data["title"]
            content    = data["userInput"]
            product_id = data["product_id"]
            
            Review.objects.create(
                title   = title,
                content = content,
                image = 'https://cdn.pixabay.com/photo/2022/05/20/08/55/pasta-7209002_1280.jpg',
                # user_id = request.user.id,
                user_id = 1,
                product_id = product_id
                )

            return JsonResponse({'message':'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({"message": 'KEY_ERROR'}, status = 400)

    def get(self, request):
        try:
            product_id = request.GET.get('productId', None)
            search     = request.GET.get('search', None)
            photo     = request.GET.get('photo', None)
            offset     = int(request.GET.get('offset', 0))
            limit      = int(request.GET.get('limit', 10))
            
            filter_set = {}

            if product_id:
                filter_set["product_id"] = product_id

            if search:
                filter_set["title__contains"] = search
            
            if photo:
                filter_set["image__contains"] = photo

            reviews = Review.objects.filter(**filter_set).order_by('-id')[offset:offset+limit]
            review_count = Review.objects.all().count()
            review_list = [{
                "id"       : review.id,
                "userId"   : User.objects.get(id=review.user_id).email,
                "title"    : review.title,
                "userInput": review.content,
                "imageSrc" : review.image,
                "date"     : review.created_at.strftime('%Y''-''%m''-''%d'),
            } for review in reviews]
    
            return JsonResponse({ "total_review":review_count, "review_list":review_list }, status=200) 

        except KeyError:
            return JsonResponse({"message": 'KEY_ERROR'}, status = 400)    

    @login_required
    def patch(self, request, review_id):
        try:
            cart_data = json.loads(request.body)

            content   = cart_data["userInput"]
            
            review = Review.objects.get(user_id = request.user.id, review_id = review_id)
            review.content = content
            review.save()

            return JsonResponse({"message":"UPDATE SUCCESS"}, status=200) 

        except KeyError:
            return JsonResponse({"message": 'KEY_ERROR'}, status = 400)
        except Review.DoesNotExist:
            return JsonResponse({"message": 'Not found Data'}, status = 400)    

    @login_required
    def delete(self, request, review_id):
        Review.objects.filter(user_id = request.user.id, id = review_id).delete()
        return JsonResponse({"message": 'SUCCESS'},status=200)