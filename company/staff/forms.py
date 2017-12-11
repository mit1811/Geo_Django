from django import forms
from .models import Recuiter,Applicant
from django.contrib.auth.models import User

class LoginForm(forms.Form):    
	username = forms.CharField()    
	password = forms.CharField(widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
	class Meta:
		model=Recuiter
		fields=[
		"recuitername",
		]

class ResumeForm(forms.ModelForm):
	class Meta:
		model=Applicant
		fields=[
		"fname",
		"lname",
		"description",
		"uniname",
		"email",
		"languagesknow",
		"contactnumber",
		]

class SearchForm(forms.ModelForm):
	class Meta:
		model=Recuiter
		fields=[
		"search",
		]

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=[
				'username',
				'first_name',
				'email',
			]
	def clean_password2(self):
		cd=self.cleaned_data
		if cd['password']!=cd ['password2']:
			raise forms.ValidationError('password not match')
		return cd['password2']	


			


