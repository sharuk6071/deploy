from django.shortcuts import render
import json
from .decorators import *
from django.views import View
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import ido
from . serializers import idoSerializer
from django.http import StreamingHttpResponse

# Create your views here.
def index(request):
    return render(request,'sai/index.html')


class Listido(APIView):

    def get(self,request):
        ido1=ido.objects.all()
        serializer=idoSerializer(ido1,many=True)
        return Response(serializer.data)


class Viewido(View):

    @method_decorator(ido_json)
    def post(self, request):
        json_data = request.json
