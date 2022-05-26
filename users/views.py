import json, re, bcrypt

from django.http import JsonResponse
from django.views import View

from users.models import User


class SignupView(View):
    def post(self, request):
        try:
            user_data = json.loads(request.body)
            
            name               = user_data['name']
            email              = user_data["email"]
            password           = user_data["password"]
            phone_number       = user_data["phoneNumber"]
            birth              = user_data["birth"]
            agreement          = user_data["agreement"]
            REGEX_EMAIL        = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            REGEX_PASSWORD     = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
            REGEX_PHONE_NUMBER = '^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$'
            REGEX_BIRTHDAY     = '^(19[0-9][0-9]|20\d{2})-(0[0-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$'

            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({"message":"INVALID_EMAIL"}, status=400)

            if not re.match(REGEX_PASSWORD, password):
                return JsonResponse({"message":"INVALID_PASSWORD "}, status=400)
            
            if not re.match(REGEX_PHONE_NUMBER, phone_number):
                return JsonResponse({"message":"INVALID_PHONE_NUMBER"}, status=400)

            if not re.match(REGEX_BIRTHDAY, birth):
                return JsonResponse({"message":"INVALID_BIRTHDAY"}, status=400)    

            if User.objects.filter(email = email).exists():
                return  JsonResponse({"message":"INVALID_EMAIL"}, status=400)  

            hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user = User(
                name         = name,
                email        = email,
                password     = hash_password,
                phone_number = phone_number,
                birth        = birth,
                agreement    = agreement
                )
            user.save()
            return JsonResponse({"message": "SUCCESS"}, status = 201)
        except KeyError:
            return JsonResponse({"message": 'KeyError'}, status = 400)  