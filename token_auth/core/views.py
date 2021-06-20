from django.shortcuts import render

# import APIView class so we can inhert it in our view class (so we cna use IsAuthendicated)
from rest_framework.views import APIView 
from rest_framework.response import Response

# let force authentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


# for data entry 
from rest_framework.parsers import JSONParser
from .models import register
from .serializers import UserSerializer

# custom json response
import json
from django.http import Http404, HttpResponse, JsonResponse

# Create your views here.
class HelloView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'message':'Hello World'}
        return Response(content)


class user_list(APIView):

    permission_classes = (IsAuthenticated,)


    def get(self, request):
        #all_registered = register.objects.all()
        #serializer = UserSerializer(all_registered, many=True)
        data = {"status":"operation_not_allowed"}
        #data['status'] = 'operation_not_allowed'
        json_data = json.dumps(data)
        return JsonResponse(json_data, status=500, safe=False)  
        #return JsonResponse(serializer.data, safe=False)


    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {'status':'successful'}
            #data['status'] = 'successful'
            json_data = json.dumps(data)
            return JsonResponse(json_data, status=201, safe=False)
            #return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)


