
import json

from django.views import View

from core.utils import token_reader


class Review(View):
    @token_reader
    def post(self, request):
        review_data = json.loads(request.body)

        title = review_data["title"]
        content = review_data["uesrInput"]
        user = request.user