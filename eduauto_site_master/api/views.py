from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Display all the users in the database
class UserListAPIView(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		users = User.objects.all().values()

		return Response({'users': users})


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.filter() 
    serializer_class = UserCreateUpdateSerializer


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.filter() 
    serializer_class = UserSerializer  
  

class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.filter() 
    serializer_class = UserSerializer
 

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.filter() 
    serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)	
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)	



