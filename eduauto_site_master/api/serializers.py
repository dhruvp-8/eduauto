from rest_framework.serializers import CharField, EmailField, ValidationError, ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField, HyperlinkedIdentityField
from django.contrib.auth.models import User
from django.db.models import Q

import random
import string

allowed_chars = ''.join((string.ascii_letters, string.digits))
unique_id = ''.join(random.choice(allowed_chars) for _ in range(32))  

# User Management Serializers
class UserSerializer(ModelSerializer):
	
	class Meta:
		model = User
		fields = [
			'id',
			'first_name',
			'last_name',
			'username',
			'email',
			'password',
		]

class UserCreateSerializer(ModelSerializer):
	email = EmailField(required=True)
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'username',
			'email',
			'password',
		]

		extra_kwargs = {"password":{"write_only":True}}
	def create(self, validated_data):
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		user_obj = User(
			first_name = first_name,
			last_name = last_name,
			username = username,
			email = email
		)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data
		
class UserCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'username',
			'email',
			'password',
		]

class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField(required=False, allow_blank=True)
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'token',
		]
		extra_kwargs = {"password":{ "write_only": True }}

	def validate(self, data):
		user_obj = None
		username = data.get("username", None)
		password = data["password"]
		if not username:
			raise ValidationError("Username is required to login.")

		user = User.objects.filter(Q(username=username)).distinct()
		if user.exists() and user.count() == 1:
			user_obj = user.first()
		else:
			raise ValidationError("This Username is not valid.")

		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("Incorrect Credentials. Please Try again")
			if user_obj.is_active == 0:
				raise ValidationError("User is not active")


		data["token"] = unique_id			

		return data	