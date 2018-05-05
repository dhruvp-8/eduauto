from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from .serializers import *

urlpatterns = [
	# Register the URL Routes here
	url(r'^users/$', UserListAPIView.as_view() ,name = 'userlist'),
	url(r'^users/create/$', UserCreateAPIView.as_view(), name='create'),
    url(r'^users/(?P<pk>[\w-]+)/$', UserDetailAPIView.as_view(), name='detail'),
    url(r'^users/(?P<pk>[\w-]+)/edit/$', UserUpdateAPIView.as_view(), name='update'),   
    url(r'^users/(?P<pk>[\w-]+)/delete/$', UserDeleteAPIView.as_view(), name='delete'),
	url(r'^user/login/$', UserLoginAPIView.as_view(), name='login'),

	# Student Data
	url(r'^branch/$', getBranch.as_view(), name='branch'),	
	url(r'^standard/$', getStandard.as_view(), name='standard'),
	url(r'^studentlist/(?P<branch>.*)/(?P<standard>\d+)/$', getStudentList.as_view(), name='get_student_list'),
	url(r'^storeAttendance/$', storeAttendance.as_view(), name='create_attendance'),
	url(r'^attendance/(?P<user_id>\d+)/$', calculateAttendance.as_view(), name='calculate_attendance'),
	url(r'^attendance/(?P<user_id>\d+)/(?P<start_date>([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])))/(?P<end_date>([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])))/$', calculateAttendanceByRangeDate.as_view(), name='calculate_attendance_by_range_date'),
	url(r'^attendance/(?P<user_id>\d+)/(?P<specific_date>([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])))/$', calculateAttendanceBySpecificDate.as_view(), name='calculate_attendance_by_specific_date'),		
]