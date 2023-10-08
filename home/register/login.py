from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from home.serializers import LoginSerializer,RegisterSerializer
from home.models import UsersModel
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UsersLogin(APIView):
    def post(self,request):
        data = request.data
        serial = LoginSerializer(data=data)
        if not serial.is_valid():
            return Response({"status": False,"Message": serial.errors})
        user = authenticate(username= serial['username'],password = serial['password'])
        if not user:
            return Response({"status":False,"message":"Invalid Credentials"})
        token, _ = Token.objects.get_or_create(user=user)
        return Response(token)

        