from django.shortcuts import render
from .user import User
from drf_yasg.utils import swagger_auto_schema
from quizzes.serializer import UserSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from bson import json_util
from bson.json_util import dumps
import json

# from rest_framework.permissions import AllowAny
# Create your views here.

class userView(APIView):
    # permission_classes = [AllowAny]
    # @swagger_auto_schema(
    #     request_body=UserSerializer
    # )
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            user = User()
            username = serializer.data["username"]
            password = serializer.data["password"]
            response = user.create_user(username=username, password=password)
            return Response({"success":True,"data":response,"error":None}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success":False,"data":None,"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        try:
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            user = User()
            username = serializer.data["username"]
            password = serializer.data["password"]
            response = user.verify_user(username=username, password=password)
            # print(response)
            # if isinstance(response, dict) and '_id' in response:
            # response =dumps(response)
            # response  = dumps(response, indent = 2) 
            print(response)
            return Response({"success":True,"data":response,"error":None}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success":False,"data":None,"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)