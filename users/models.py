from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self,*args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img=Image.open(self.image.path)

		if img.height > 50 or img.width > 50:
			output_size=(100,100)
			img.thumbnail(output_size)
			img.convert('RGB').save(self.image.path)


class Grade(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	grade=models.CharField(max_length=15)

	def __str__(self):
		return f'{self.user.username} Grade'

class Course(models.Model):
	user=models.ManyToManyField(User,related_name="course_user_connect")
	code=models.CharField(max_length=15)
	name=models.CharField(max_length=100)
	semester=models.CharField(max_length=100)
	description=models.TextField()

	def __str__(self):
		return f'{self.name}'

	def get_absolute_url(self):
		return reverse('courseregister')

class Assignment(models.Model):
	course=models.ForeignKey(Course,on_delete=models.CASCADE)
	#user=models.ManyToManyField(User,related_name="assignment_user_connect")
	name=models.CharField(max_length=15)
	description=models.TextField(max_length=1000000000)
	file=models.FileField(blank=True)

	def __str__(self):
		return f'{self.name} Assignment'

	def save(self,*args, **kwargs):
		super(Assignment, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('assignmentdetail',kwargs={'pk':self.pk})

class GradeAssignments(models.Model):
	course=models.ForeignKey(Course,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE)
	grade=models.CharField(max_length=15)

	def __str__(self):
		return f'{self.assignment} Grade'

	def save(self,*args, **kwargs):
		super(GradeAssignments, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('gradeassignments_create')