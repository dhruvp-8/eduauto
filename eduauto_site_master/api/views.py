from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *
from datetime import datetime
from datetime import timedelta
from eduauto_site_master import settings

from django.core.files.storage import FileSystemStorage
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
class UserCreateAPIView(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, *args, **kwargs):
		data = request.data
		usern = User.objects.filter(Q(username=data["username"])).distinct()
		usere = User.objects.filter(Q(email=data["email"])).distinct()
		if usern.exists() and usern.count() == 1:
			return Response({'error': 'Username already exists.'})
		elif usere.exists() and usere.count() == 1:
			return Response({'error': 'Email already exists.'})
		else:	
			first_name = data['first_name']
			last_name = data['last_name']
			username = data['username']
			email = data['email']
			password = data['password']
			u_type = data['u_type']
			user_obj = User(
				first_name = first_name,
				last_name = last_name,
				username = username,
				email = email
			)
			user_obj.set_password(password)
			user_obj.save()

			user_mapping_obj = EaUserMapping()
			user_mapping_obj.user_id = user_obj.id
			user_mapping_obj.user_type = u_type
			user_mapping_obj.save()

			if u_type == "student":
				student_details_obj = EaStudentDetails()
				student_details_obj.user_id = user_obj.id
				# Create Roll Number for student
				student_details_obj.roll_no = user_obj.id
				student_details_obj.save()

				academic_history_obj = EaAcademicHistory()
				academic_history_obj.user_id = user_obj.id
				academic_history_obj.save()

				# Create Fees History of Student
				fees_obj = EaFeesAccounts()
				fees_obj.user_id = user_obj.id
				fees_obj.save()
			elif u_type == "teacher":
				teacher_details_obj = EaTeacherDetails()
				teacher_details_obj.user_id = user_obj.id
				teacher_details_obj.save()
			else:
				user_obj.is_staff = 1
				user_obj.save()
				
			return Response({'success': 'User created successfully', 'first_name': first_name, 'last_name': last_name, 'username': username, 'email': email})

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
		return Response({'branch': branch}, status=HTTP_200_OK)

# Get List of all Standards for selection
class getStandard(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		standard = EaStudentDetails.objects.values_list('standard', flat=True).order_by('standard').distinct()
		return Response({'standard': standard}, status=HTTP_200_OK)

# Get List of all Subjects for selection
class getSubjects(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		subjects = EaStudentDetails.objects.values_list('subjects_enrolled', flat=True).order_by('standard').distinct()
		fin_subs = set()
		for i in range(0, len(subjects)):
			r = subjects[i].split(";")
			for j in range(0, len(r)):
				fin_subs.add(r[j])
		subs = []
		for i in fin_subs:
			if i != '':
				subs.append(i)		
		return Response({'subjects': subs}, status=HTTP_200_OK)


# Get Student Data List for taking the Attendance
class getStudentList(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		studentlist = []
		branch = self.kwargs.get('branch')
		standard = self.kwargs.get('standard')
		subject = self.kwargs.get('subject')
		roll_no = EaStudentDetails.objects.filter(branch=branch, standard=standard, subjects_enrolled__contains=subject).values('roll_no','user_id')
		user_type = 'student'
		for i in range(0,len(roll_no)):
			fin = {}
			name = User.objects.filter(id=roll_no[i]['user_id']).values('id','first_name', 'last_name')
			fin['user_id'] = roll_no[i]['user_id']
			fin['user_type'] = user_type
			fin['roll_no'] = roll_no[i]['roll_no']
			fin['name'] = name[0]['first_name'] + ' ' + name[0]['last_name']
			studentlist.append(fin)
		return Response({'studentlist': studentlist}, status=HTTP_200_OK)

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

		return Response({'user_id': user_id, 'present_days': present_days, 'absent_days':absent_days, 'total_teaching_days': total_teaching_days,'percentage': percent}, status=HTTP_200_OK)

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
		
		return Response({'user_id': user_id, 'start_date': start_date, 'end_date': end_date, 'total_teaching_days': total_teaching_days, 'present_days': present_days, 'absent_days': absent_days, 'percentage': percent}, status=HTTP_200_OK)

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

		return Response({'user_id': user_id, 'specific_date': specific_date, 'present_days': present_days, 'absent_days':absent_days, 'total_teaching_days': total_teaching_days}, status=HTTP_200_OK)

# Add Student Details 
class storeStudentDetails(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, *args, **kwargs):
		data = request.data
		user_id = int(data["user_id"])
		standard = data["standard"]
		school = data["school"]
		address = data["address"]
		branch = data["branch"]
		emergency_number = data["emergency_number"]
		year_of_joining = datetime.now().year
		birthdate = data["birthdate"]
		contact_no = int(data["contact_no"])
		refs = data["refs"]
		subjects_enrolled = data["subjects_enrolled"]
		stream = data["stream"]
		board = data["board"]
		total_fees = int(data["total_fees"])
		fees_paid = int(data["fees_paid"])
		year_of_leaving = data["year_of_leaving"]

		student_details_obj = EaStudentDetails.objects.get(user_id=user_id)
		student_details_obj.standard = standard
		student_details_obj.school = school
		student_details_obj.address = address
		student_details_obj.emergency_number = emergency_number
		student_details_obj.year_of_joining = year_of_joining
		student_details_obj.birthdate = birthdate
		student_details_obj.contact_no = contact_no
		student_details_obj.refs = refs
		student_details_obj.subjects_enrolled = subjects_enrolled
		student_details_obj.year_of_leaving = year_of_leaving
		student_details_obj.stream = stream
		student_details_obj.board = board
		
		if total_fees - fees_paid > 0:
			student_details_obj.save()

			fees_obj = EaFeesAccounts.objects.get(user_id=user_id)
			fees_obj.total_fees = total_fees
			fees_obj.fees_paid = fees_paid
			fees_obj.paid_status = 0
			fees_obj.save()
		elif total_fees - fees_paid == 0:
			student_details_obj.save()

			fees_obj = EaFeesAccounts.objects.get(user_id=user_id)
			fees_obj.total_fees = total_fees
			fees_obj.fees_paid = fees_paid
			fees_obj.paid_status = 1
			fees_obj.save()
		else:
			return Response({'error': 'Fees Paid cannot be more than Total Fees.'}, status=HTTP_400_BAD_REQUEST)	
		return Response({'success': 'Student created successfully', 'roll_no': student_details_obj.roll_no}, status=HTTP_200_OK)		

# Get all the news present till date along with the comments
class getNews(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		news = EaNewsFeed.objects.all().order_by('-date').values()
		for i in range(0,len(news)):
			file_name = news[i]['file_name'] + '.' + news[i]['file_type']
			news[i]['file_name'] = file_name
			comments = EaNewsComments.objects.filter(news_id=news[i]['news_id']).exclude(description='').values()
			news[i]['comments'] = comments
			total_likes = EaNewsComments.objects.filter(news_id=news[i]['news_id'], likes=1).count()
			news[i]['total_likes'] = total_likes

		return Response({'news': news}, status=HTTP_200_OK)

# Get Only Recent/last n news posts with comments 
class getRecentNews(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		n = int(self.kwargs.get('no'))
		news = EaNewsFeed.objects.filter().order_by('-date').values()[:n]
		for i in range(0,len(news)):
			file_name = news[i]['file_name'] + '.' + news[i]['file_type']
			news[i]['file_name'] = file_name
			comments = EaNewsComments.objects.filter(news_id=news[i]['news_id']).exclude(description='').values()
			news[i]['comments'] = comments
			total_likes = EaNewsComments.objects.filter(news_id=news[i]['news_id'], likes=1).count()
			news[i]['total_likes'] = total_likes

		return Response({'news': news}, status=HTTP_200_OK)

# Get news based on popularity/likes
class getNewsBasedonPopularity(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		news = EaNewsFeed.objects.all().order_by('-date').values()
		total_likes_s = []
		for i in range(0,len(news)):
			comments = EaNewsComments.objects.filter(news_id=news[i]['news_id']).exclude(description='').values()
			ts = EaNewsComments.objects.filter(news_id=news[i]['news_id'], likes=1).count()
			total_likes_s.append((news[i]['news_id'], ts))

		sorted_vals = sorted(total_likes_s, key=lambda x:x[1])
		sorted_vals = sorted_vals[::-1]
		fin_news = []
		for j in range(0, len(sorted_vals)):
			news = EaNewsFeed.objects.filter(news_id=sorted_vals[j][0]).values()
			for i in range(0,len(news)):
				file_name = news[i]['file_name'] + '.' + news[i]['file_type']
				news[i]['file_name'] = file_name
				comments = EaNewsComments.objects.filter(news_id=news[i]['news_id']).exclude(description='').values()
				news[i]['comments'] = comments
				total_likes = EaNewsComments.objects.filter(news_id=news[i]['news_id'], likes=1).count()
				news[i]['total_likes'] = total_likes
			fin_news.append(news[0])	

		return Response({'news': fin_news}, status=HTTP_200_OK)

# Get News Based on ID
class getNewsOnId(APIView):
	renderer_classes = (JSONRenderer, )

	def get(self, request, *args, **kwargs):
		news_id = int(self.kwargs.get('news_id'))
		news = EaNewsFeed.objects.filter(news_id=news_id).values()
		comments = EaNewsComments.objects.filter(news_id=news_id).exclude(description='').values()
		total_likes = EaNewsComments.objects.filter(news_id=news_id, likes=1).count()
		tmp = news[0]
		tmp["comments"] = comments
		tmp["total_likes"] = total_likes

		return Response({'news': tmp}, status=HTTP_200_OK)

# Add news to the feed
class addNewsFeed(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, *args, **kwargs):
		ea_news_feed_obj = EaNewsFeed()
		data = request.data
		user_id = data["user_id"]
		if 'myfile' in data.keys() and 'description' in data.keys():
			description = data["description"]
			myfile = data["myfile"] 
			tmp = str(myfile)
			im = tmp.split(".")
			if len(im) > 2:
				return Response({'error': 'File name is should not contain more than 1 dot.'}, status=HTTP_400_BAD_REQUEST)
			else:
				im_name = im[0]
				im_type = im[1]
				dt = datetime.now()
				ml = str(dt.microsecond)
				f_im_name = im_name + '_' + ml
				if im_type.lower() == 'jpg' or im_type.lower() == 'png' or im_type.lower() == 'bmp' or im_type.lower() == 'jpeg' or im_type.lower() == 'pdf' or im_type.lower() == 'txt' or im_type.lower() == 'docx' or im_type.lower() == 'xlsx':
					ks = EaNewsFeed.objects.all().last()
					news_id = int(ks.news_id) + 1
					ea_news_feed_obj.news_id = news_id
					ea_news_feed_obj.user_id = user_id
					ea_news_feed_obj.description = description
					ea_news_feed_obj.file_name = f_im_name
					ea_news_feed_obj.file_type = im[1]
					ea_news_feed_obj.save()
					fin_name = f_im_name + '.' + im_type
					fs = FileSystemStorage(location=settings.MEDIA_STORAGE_ROOT)
					filename = fs.save(fin_name, myfile)
					return Response({'success': 'News Feed created successfully.', 'news_id': news_id, 'user_id': user_id, 'date': ea_news_feed_obj.date}, status=HTTP_200_OK)
				else:
					return Response({'error': 'File type must be jpg, jpeg, bmp, png, pdf, txt, docx, xlsx.'}, status=HTTP_400_BAD_REQUEST)
		elif 'description' in data.keys() and not 'myfile' in data.keys():
			description = data["description"]
			ks = EaNewsFeed.objects.all().last()
			news_id = int(ks.news_id) + 1
			ea_news_feed_obj.news_id = news_id
			ea_news_feed_obj.user_id = user_id
			ea_news_feed_obj.description = description
			ea_news_feed_obj.save()
			return Response({'success': 'News Feed created successfully.', 'news_id': news_id, 'user_id': user_id, 'date': ea_news_feed_obj.date}, status=HTTP_200_OK)
		elif 'myfile' in data.keys() and not 'description' in data.keys():
			myfile = data["myfile"] 
			tmp = str(myfile)
			im = tmp.split(".")
			if len(im) > 2:
				return Response({'error': 'File name is should not contain more than 1 dot.'}, status=HTTP_400_BAD_REQUEST)
			else:
				im_name = im[0]
				im_type = im[1]
				dt = datetime.now()
				ml = str(dt.microsecond)
				f_im_name = im_name + '_' + ml
				if im_type.lower() == 'jpg' or im_type.lower() == 'png' or im_type.lower() == 'bmp' or im_type.lower() == 'jpeg' or im_type.lower() == 'pdf' or im_type.lower() == 'txt' or im_type.lower() == 'docx' or im_type.lower() == 'xlsx':
					ks = EaNewsFeed.objects.all().last()
					news_id = int(ks.news_id) + 1
					ea_news_feed_obj.news_id = news_id
					ea_news_feed_obj.user_id = user_id
					ea_news_feed_obj.file_name = f_im_name
					ea_news_feed_obj.file_type = im[1]
					ea_news_feed_obj.save()
					fin_name = f_im_name + '.' + im_type
					fs = FileSystemStorage(location=settings.MEDIA_STORAGE_ROOT)
					filename = fs.save(fin_name, myfile)
					return Response({'success': 'News Feed created successfully.', 'news_id': news_id, 'user_id': user_id, 'date': ea_news_feed_obj.date}, status=HTTP_200_OK)
				else:
					return Response({'error': 'File type must be jpg, jpeg, bmp, png, pdf, txt, docx, xlsx.'}, status=HTTP_400_BAD_REQUEST)	 
		else:
			return Response({'error': 'Please Select Description or Image to continue'}, status=HTTP_400_BAD_REQUEST)			

# Add Comments to the News Feed
class addComments(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, *args, **kwargs):
		data = request.data
		ks = EaNewsComments.objects.all().last()
		comment_id = int(ks.comment_id) + 1
		news_id = data["news_id"]
		user_id = data["user_id"]
		description = data["description"]

		if description != '':
			ea_news_comment_obj = EaNewsComments()
			ea_news_comment_obj.comment_id = comment_id
			ea_news_comment_obj.news_id = news_id
			ea_news_comment_obj.user_id = user_id
			ea_news_comment_obj.description = description

			ea_news_comment_obj.save()
			return Response({'success': 'Comment saved successfully.', 'comment_id': comment_id, 'user_id': user_id, 'date': ea_news_comment_obj.date}, status=HTTP_200_OK)
		else:
			return Response({'error': 'Please Enter the comment to continue.'}, status=HTTP_400_BAD_REQUEST)

# Like a particular News Feed
class addLikes(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, *args, **kwargs):
		data = request.data
		ks = EaNewsComments.objects.all().last()
		comment_id = int(ks.comment_id) + 1
		news_id = data["news_id"]
		user_id = data["user_id"]
		ch = EaNewsComments.objects.filter(news_id=news_id,user_id=user_id).count()
		if ch < 1:
			ea_news_comment_obj = EaNewsComments()
			ea_news_comment_obj.comment_id = comment_id
			ea_news_comment_obj.news_id = news_id
			ea_news_comment_obj.user_id = user_id
			ea_news_comment_obj.likes = True

			ea_news_comment_obj.save()
			return Response({'success': 'Like saved successfully.', 'like_id': comment_id, 'user_id': user_id, 'date': ea_news_comment_obj.date}, status=HTTP_200_OK)
		else:
			kp = EaNewsComments.objects.filter(news_id=news_id, user_id=user_id, likes=0).count()
			if kp == 1:
				ea_news_comment_obj = EaNewsComments.objects.get(news_id=news_id, user_id=user_id, likes=0)
				ea_news_comment_obj.likes = True

				ea_news_comment_obj.save()
				return Response({'success': 'Like Updated successfully.', 'like_id': ea_news_comment_obj.comment_id, 'user_id': user_id, 'date': ea_news_comment_obj.date}, status=HTTP_200_OK)
			else:
				return Response({'error': 'This User has already liked the post.'}, status=HTTP_400_BAD_REQUEST)

# Unlike a particular news feed
class removeLikes(APIView):
	renderer_classes = (JSONRenderer, )

	def post(self, request, *args, **kwargs):
		data = request.data
		news_id = data["news_id"]
		user_id = data["user_id"]

		ch = EaNewsComments.objects.filter(news_id=news_id,user_id=user_id).count()
		if ch > 0:
			kp = EaNewsComments.objects.filter(news_id=news_id, user_id=user_id, likes=1).count()
			if kp == 1:
				ea_news_comment_obj = EaNewsComments.objects.get(news_id=news_id, user_id=user_id, likes=1)
				ea_news_comment_obj.likes = False

				ea_news_comment_obj.save()
				return Response({'success': 'Unliked the post successfully.', 'unlike_id': ea_news_comment_obj.comment_id, 'user_id': user_id, 'date': ea_news_comment_obj.date}, status=HTTP_200_OK)
			else:
				return Response({'error': 'This User has already unliked the post.'}, status=HTTP_400_BAD_REQUEST)
		else:
			return Response({'error': 'User has not liked this post.'}, status=HTTP_400_BAD_REQUEST)
		