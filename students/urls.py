from django.urls import path
from .views import *

urlpatterns = [
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/create/", CourseCreateView.as_view(), name="course-create"),
    path("courses/<int:pk>/edit/", CourseUpdateView.as_view(), name="course-edit"),
    path("courses/<int:pk>/delete/", CourseDeleteView.as_view(), name="course-delete"),

    path("", StudentListView.as_view(), name="student-list"),
    path("students/create/", StudentCreateView.as_view(), name="student-create"),
    path("students/<int:pk>/edit/", StudentUpdateView.as_view(), name="student-edit"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student-delete"),
]