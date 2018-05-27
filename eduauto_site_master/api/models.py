from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class EaStudentDetails(models.Model):
	user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
	standard = models.PositiveSmallIntegerField(blank=True)
	school = models.CharField(max_length=255,blank=True)
	address = models.CharField(max_length=255, blank=True)
	branch = models.CharField(max_length=255, blank=True)
	emergency_number = models.BigIntegerField(blank=True)
	roll_no = models.IntegerField()
	year_of_joining = models.CharField(max_length=4,blank=True)
	birthdate = models.DateField(blank=True)
	contact_no = models.BigIntegerField(blank=True)
	refs = models.TextField(blank=True)
	subjects_enrolled = models.TextField(blank=True)
	year_of_leaving = models.CharField(max_length=4,blank=True)
	stream = models.CharField(max_length=255, blank=True)
	board = models.CharField(max_length=255, blank=True)

	class Meta:
		managed = False
		db_table = 'ea_student_details'

class EaTeacherDetails(models.Model):
	user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
	standard = models.IntegerField(blank=True)
	subject = models.CharField(max_length=255, blank=True) 
	address = models.CharField(max_length=255, blank=True)
	birthdate = models.DateField(blank=True)
	year_of_joining = models.DateTimeField(blank=True)
	activated_status = models.BooleanField(blank=True)
	contact_no = models.BigIntegerField(blank=True)
	salary = models.IntegerField(blank=True)
	bank_details = models.TextField(blank=True)

	class Meta:
		managed = False
		db_table = 'ea_teacher_details'

class EaAttendance(models.Model):
	att_id = models.IntegerField(primary_key=True)
	user_id = models.IntegerField()
	roll_no = models.IntegerField()
	date = models.DateTimeField(default=datetime.now, blank=True)
	user_type = models.CharField(max_length=255)
	attend_status = models.BooleanField()

	class Meta:
		managed = False
		db_table = 'ea_attendance'

class EaAcademicHistory(models.Model):
	user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
	university = models.CharField(max_length=255,blank=True)
	year_of_passing = models.DateField(blank=True)
	percentage_scored = models.IntegerField(blank=True)

	class Meta:
		managed = False
		db_table = 'ea_academic_history'

class EaUserMapping(models.Model):
	user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=255)

	class Meta:
		managed = False
		db_table = 'ea_user_mapping'

class EaNewsFeed(models.Model):
	news_id = models.IntegerField(primary_key=True)
	user = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
	description = models.TextField()
	file_name = models.CharField(max_length=255, blank=True)
	file_type = models.CharField(max_length=255, blank=True)
	date = models.DateTimeField(default=datetime.now, blank=True)

	class Meta:
		managed = False
		db_table = 'ea_news_feed'

class EaNewsComments(models.Model):
	comment_id = models.AutoField(primary_key=True)
	news = models.ForeignKey(EaNewsFeed, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	likes = models.BooleanField(default=False)
	date = models.DateTimeField(default=datetime.now, blank=True)

	class Meta:
		managed = False
		db_table = 'ea_news_comments'

class EaFeesAccounts(models.Model):
	trans_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	paid_status = models.BooleanField(default=False)
	fees_paid = models.IntegerField(blank=True)
	total_fees = models.IntegerField(blank=True)
	date = models.DateTimeField(default=datetime.now, blank=True)

	class Meta:
		managed = False
		db_table = 'ea_fees_accounts'