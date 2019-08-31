from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from users.models import Course, Assignment, GradeAssignments
from users.forms import AssignmentSubmitForm
#from django.views.generic.edit import FormMixin


def home(request):
	context={
		'courses': Course.objects.filter(user=request.user)
	}
	return render(request,'users/courselist.html',context)

class CourseListView(ListView):
	model = Course
	template_name='users/courselist.html'
	context_object_name='courses'

	def get_queryset(self):
		return self.request.user.course_user_connect.all()

class CourseDetailView(DetailView):
	model = Course
	template_name='users/assignmentlist.html'


class CourseCreateView(CreateView):
	model = Course
	fields=['code','name','semester','description']

	def form_valid(self,form):
		return super().form_valid(form)


class AssignmentListView(ListView):
	model = Assignment
	template_name='users/assignmentlist.html'
	context_object_name='assignments'

	def get_queryset(self,**kwargs):
		return Assignment.objects.filter(course=self.kwargs['pk'])

class AssignmentDetailView(DetailView):
	model = Assignment
	template_name='users/assignmentdetail.html'

class AssignmentCreateView(CreateView):
	model = Assignment
	fields=['course','name','description','file']
	
	def form_valid(self,form):
		return super().form_valid(form)

class GradeAssignmentsListView(ListView):
	model = GradeAssignments
	template_name='users/gradeassignmentslist.html'
	context_object_name='gradeassignments'

	def get_queryset(self,**kwargs):
		return GradeAssignments.objects.filter(user=self.kwargs['pk'])

class GradeAssignmentsCreateView(CreateView):
	model= GradeAssignments
	fields=['user','course','assignment','grade']

	def form_valid(self,form):
		return super().form_valid(form)

def about(request):
	return render(request,'dashboard/about.html',{'title':'About'}) 