from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
import datetime

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Display all the users in the database
class UserListAPIView(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		users = User.objects.all().values()

		return Response({'users': users})

# Update the data of the user into the DB
class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.filter() 
    serializer_class = UserCreateUpdateSerializer

# Delete a specific user from DB
class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.filter() 
    serializer_class = UserSerializer  
  
# Fetch all possible users
class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.filter() 
    serializer_class = UserSerializer
 
# Allow to create a new user into DB
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.filter() 
    serializer_class = UserCreateSerializer

# Allow user to login to the system
class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)	
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# Get List of all the branches for selection
class getBranch(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		branch = EaStudentDetails.objects.values_list('branch', flat=True).order_by('branch').distinct()
		return Response({'branch': branch})

# Get List of all Standards for selection
class getStandard(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		standard = EaStudentDetails.objects.values_list('standard', flat=True).order_by('standard').distinct()
		return Response({'standard': standard})

# Get Student Data List for taking the Attendance
class getStudentList(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		studentlist = []
		branch = self.kwargs.get('branch')
		standard = self.kwargs.get('standard')
		roll_no = EaStudentDetails.objects.filter(branch=branch, standard=standard).values('roll_no','s_id')
		user_type = 'student'
		for i in range(0,len(roll_no)):
			fin = {}
			name = User.objects.filter(id=roll_no[i]['s_id']).values('id','first_name', 'last_name')
			fin['user_id'] = roll_no[i]['s_id']
			fin['user_type'] = user_type
			fin['roll_no'] = roll_no[i]['roll_no']
			fin['name'] = name[0]['first_name'] + ' ' + name[0]['last_name']
			studentlist.append(fin)
		return Response({'studentlist': studentlist})

# Enter Attendance Data in the DB
class storeAttendance(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, *args, **kwargs):
		data = request.data
		attendance_data = data["attendance"]
		if len(attendance_data) != 0:
			eaAttendance = EaAttendance()
			for i in range(0, len(attendance_data)):
				user_id = attendance_data[i]["user_id"]
				roll_no = attendance_data[i]["roll_no"]
				user_type = attendance_data[i]["user_type"]
				attend_status = attendance_data[i]["attend_status"]

				eaAttendance.user_id = user_id
				eaAttendance.roll_no = roll_no
				eaAttendance.user_type = user_type
				eaAttendance.attend_status = attend_status

				eaAttendance.save()
			return Response(status=HTTP_200_OK)
		else:
			return Response(status=HTTP_400_BAD_REQUEST)




