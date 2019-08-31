from django.db.models.signals import post_save
from django.contrib.auth.models import User
#from dashboard.models import Course
from django.dispatch import receiver
from .models import Profile, Grade, Assignment, Course

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()



@receiver(post_save,sender=User)
def create_grade(sender,instance,created,**kwargs):
	if created:
		Grade.objects.create(user=instance)

@receiver(post_save,sender=User)
def create_assignment(sender,instance,created,**kwargs):
	if created:
		Assignment.objects.create(user=instance)

@receiver(post_save,sender=User)
def create_course(sender,instance,created,**kwargs):
	if created:
		Course.objects.create(user=instance)
