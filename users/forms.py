from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Grade, Assignment, Course
#from dashboard.models import Course

class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	ubid=forms.CharField()
	typeofUser=forms.ChoiceField(choices=[(1,'Student'),(2,'Professor')])

	class Meta:
		model=User
		fields=['username','ubid','email','typeofUser','password1','password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model= User
		fields= ['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']


class GradeRegisterForm(forms.ModelForm):
	class Meta:
		model = Grade
		fields = ['grade']

class AssignmentSubmitForm(forms.ModelForm):
	class Meta:
		model = Assignment
		fields = ['file']


class CourseRegisterForm(forms.ModelForm):
	choice=forms.ModelChoiceField(queryset=Course.objects.all())
	class Meta:
		model= Course
		fields= ['choice']