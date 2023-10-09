from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from home.serializers import TaskSerializer
from home.models import TaskManage
from django.core.paginator import Paginator



class ManagerTasks(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        if request.GET.get('filter_id'):
            data = request.GET.get('filter_id')
            data = int(data)
            objs = TaskManage.objects.filter(id = data)
            serial = TaskSerializer(objs,many=True)
            return Response(serial.data)
        if request.GET.get('filter_status'):
            data = request.GET.get('filter_status')
            objs = TaskManage.objects.filter(status = data)
            serial = TaskSerializer(objs,many=True)
            return Response(serial.data)
        if request.GET.get('pages'):
            try:
                page = request.GET.get('pages',1)
                page_size = 3
                page = int(page)
                objs = TaskManage.objects.all()
                paginate = Paginator(objs,page_size)
                serial = TaskSerializer(paginate.page(page),many=True)
                return Response(serial.data)
            except Exception as e:
                return Response({"Error": "No page found"})
        objs = TaskManage.objects.all()
        serial = TaskSerializer(objs,many=True)
        return Response(serial.data)

    def post(self,request):
        data = request.data
        serial = TaskSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors)