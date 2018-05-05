from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from datetime import datetime
from datetime import timedelta  

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

# Calculate Attendance
class calculateAttendance(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		user_id = int(self.kwargs.get('user_id'))
		total_teaching_days = EaAttendance.objects.filter(user_id=user_id).count()
		present_days = EaAttendance.objects.filter(user_id=user_id, attend_status=1).count()
		absent_days = EaAttendance.objects.filter(user_id=user_id, attend_status=0).count()
		percent = (present_days/total_teaching_days)*100

		return Response({'user_id': user_id, 'present_days': present_days, 'absent_days':absent_days, 'total_teaching_days': total_teaching_days,'percentage': percent})

# Calculate Attendance by range of dates
class calculateAttendanceByRangeDate(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		user_id = int(self.kwargs.get('user_id'))
		start_date = self.kwargs.get('start_date')
		end_date = self.kwargs.get('end_date')
		total_teaching_days = EaAttendance.objects.filter(user_id=user_id, date__range=[start_date, end_date]).count()
		present_days = EaAttendance.objects.filter(user_id=user_id, attend_status=1, date__range=[start_date, end_date]).count()
		absent_days = EaAttendance.objects.filter(user_id=user_id, attend_status=0, date__range=[start_date, end_date]).count()
		percent = (present_days/total_teaching_days)*100
		
		return Response({'user_id': user_id, 'start_date': start_date, 'end_date': end_date, 'total_teaching_days': total_teaching_days, 'present_days': present_days, 'absent_days': absent_days, 'percentage': percent})

# Calculate Attendance by a specific date
class calculateAttendanceBySpecificDate(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		user_id = int(self.kwargs.get('user_id'))
		specific_date = self.kwargs.get('specific_date')
		c_date = datetime.strptime(specific_date, '%Y-%m-%d') + timedelta(days=1)
		c_date = str(c_date).split(' ')
		next_date = c_date[0]
		total_teaching_days = EaAttendance.objects.filter(user_id=user_id, date__range=[specific_date, next_date]).count()
		present_days = EaAttendance.objects.filter(user_id=user_id, attend_status=1, date__range=[specific_date, next_date]).count()
		absent_days = EaAttendance.objects.filter(user_id=user_id, attend_status=0, date__range=[specific_date, next_date]).count()

		return Response({'user_id': user_id, 'specific_date': specific_date, 'present_days': present_days, 'absent_days':absent_days, 'total_teaching_days': total_teaching_days})

