from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class EaStudentDetails(models.Model):
	s_id = models.AutoField(primary_key=True)
	standard = models.PositiveSmallIntegerField()
	school = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	branch = models.CharField(max_length=255)
	emergency_number = models.BigIntegerField()
	roll_no = models.IntegerField()
	year_of_joining = models.DateTimeField()
	birthdate = models.DateField()
	contact_no = models.BigIntegerField()
	refs = models.TextField()
	fees_paid = models.IntegerField()
	subjects_enrolled = models.TextField()
	activated_status = models.BooleanField()
	year_of_leaving = models.DateTimeField()
	stream = models.CharField(max_length=255)
	board = models.CharField(max_length=255)

	class Meta:
		managed = False
		db_table = 'ea_student_details'

class EaTeacherDetails(models.Model):
	t_id = models.AutoField(primary_key=True)
	standard = models.IntegerField()
	subject = models.CharField(max_length=255) 
	address = models.CharField(max_length=255)
	birthdate = models.DateField()
	year_of_joining = models.DateTimeField()
	activated_status = models.BooleanField()
	contact_no = models.BigIntegerField()
	salary = models.IntegerField()
	bank_details = models.TextField()

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
	user_id = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
	university = models.CharField(max_length=255)
	year_of_passing = models.DateField()
	percentage_scored = models.IntegerField()

	class Meta:
		managed = False
		db_table = 'ea_academic_history'

class EaUserMapping(models.Model):
	user_id = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
	user_type = models.CharField(max_length=255)

	class Meta:
		managed = False
		db_table = 'ea_user_mapping'