from django import forms
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

	email = forms.EmailField()

	class Meta:
		#saves as if it is a user object as UserCreationForm does
		model = User

		#specifies in what worder these predefined fields show 
		fields = ["username", "email", "password1", "password2"]
