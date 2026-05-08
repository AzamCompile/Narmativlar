from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Course, Student
from .forms import CourseForm, StudentForm



class CourseListView(ListView):
    model = Course
    template_name = "course/course_list.html"
    context_object_name = "courses"


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "course/course_form.html"
    success_url = reverse_lazy("course-list")


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "course/course_form.html"
    success_url = reverse_lazy("course-list")


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "course/course_confirm_delete.html"
    success_url = reverse_lazy("course-list")




class StudentListView(ListView):
    model = Student
    template_name = "student/student_list.html"
    context_object_name = "students"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/student_form.html"
    success_url = reverse_lazy("student-list")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "student/student_form.html"
    success_url = reverse_lazy("student-list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student/student_confirm_delete.html"
    success_url = reverse_lazy("student-list")