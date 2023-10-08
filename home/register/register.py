from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from home.serializers import UserSerializer,RegisterSerializer
from home.models import UsersModel

class Users(APIView):
    def post(self,request):
        data = request.data
        serial = RegisterSerializer(data=data)
        if not serial.is_valid():
            return Response({"status": False,"Message": serial.errors})
        serial.save()
        return Response({"status":True,"Message":"User created"})