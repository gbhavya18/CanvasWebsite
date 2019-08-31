from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, GradeRegisterForm, CourseRegisterForm, AssignmentSubmitForm
from django.contrib.auth.decorators import login_required
from .models import Course, Assignment

def register(request):
	if request.method=='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your Account has been created! You are now able to login')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/userregister.html', {'form': form})

@login_required
def profile(request):
	if request.method=='POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your Account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)

	context={'u_form' :u_form,'p_form' :p_form}
	return render(request, 'users/profile.html',context)


@login_required
def grade(request):
	if request.method=='POST':
		g_form=GradeRegisterForm(request.POST, request.FILES, instance=request.user.grade)

		if g_form.is_valid():
			g_form.save()
			messages.success(request,f'Grade has been updated!')
			return redirect('grade')
	else:
		g_form=GradeRegisterForm(instance=request.user.grade)

	context={'g_form' :g_form}
	return render(request, 'users/grade.html',context)


@login_required
def courselist(request):
	context={
		'courses': request.user.course_user_connect.all()
	}
	return render(request,'users/courselist.html',context)

@login_required
def courseregister(request):
	if request.method=='POST':
		c_form=CourseRegisterForm(request.POST, request.FILES, instance=request.user)

		if c_form.is_valid():
			c_form.save()
			new_course=c_form.cleaned_data.get('choice')
			request.user.course_user_connect.add(Course.objects.get(name=new_course))
			messages.success(request,f'You have registered')
			return redirect('courselist')
	else:
		c_form=CourseRegisterForm(instance=request.user)

	context={'c_form' :c_form}
	return render(request, 'users/courseregister.html',context)
"""
@login_required
def assignmentsubmit(request):
	if request.method=='POST':
		a_form=AssignmentSubmitForm(request.POST, request.FILES, instance=request.user)
		#assignment.course=pk
		if a_form.is_valid():
			a_form.save()
			assign_submit=a_form.cleaned_data.get('file')
			request.user.assignment_user_connect.file.add(Assignment.objects.get(name=assign_submit))
			messages.success(request,f'You have submitted assignment')
			return redirect('assignmentlist')
	else:
		a_form=AssignmentSubmitForm(instance=request.user)

	context={'a_form' :a_form}
	return render(request, 'users/assignmentdetail.html',context)
"""

@login_required
def assignmentsubmit(request):
	if request.method=='POST':
		a_form=AssignmentSubmitForm(request.POST, request.FILES, instance=request.user.assignment_user_connect)

		if a_form.is_valid():
			a_form.save()
			messages.success(request,f'Your Assignment has been submitted!')
			return redirect('assignmentlist')
	else:
		a_form=ProfileUpdateForm(instance=request.user.assignment)

	context={'a_form' :a_form}
	return render(request, 'users/assignmentdetail.html',context)

@login_required
def assignmentlistsubmitted(request):
	context={
		'assignmentssubmitted': request.user.course.assignment_course_connect.all()
	}
	return render(request,'users/assignmentlist.html',context)


@login_required
def assignmentlist(request):
	context={
		'assignments': Course.assignment_course_connect.all()
	}
	return render(request,'users/assignmentlist.html',context)