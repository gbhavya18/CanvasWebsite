from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from .views import CourseListView, CourseDetailView, CourseCreateView, AssignmentListView, AssignmentDetailView, AssignmentCreateView, GradeAssignmentsCreateView, GradeAssignmentsListView
from . import views

urlpatterns = [
    path('home/', CourseListView.as_view(), name='dashboard-home'),
    path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('course/<int:pk>/', AssignmentListView.as_view(), name='assignmentlist'),
    path('assignment/<int:pk>/', AssignmentDetailView.as_view(), name='assignmentdetail'),
    path('assignmentsubmit/', user_views.assignmentsubmit, name='assignmentsubmit'),
    path('course/coursecreate/', CourseCreateView.as_view(), name='course_create'),
    path('grades/<int:pk>', GradeAssignmentsListView.as_view(), name='gradeassignmentslist'),
    path('grade/gradeassignments/', GradeAssignmentsCreateView.as_view(), name='gradeassignments_create'),
    path('assignment/assignmentcreate/', AssignmentCreateView.as_view(), name='assignment_create'),
    path('about/', views.about, name='dashboard-about'),
]