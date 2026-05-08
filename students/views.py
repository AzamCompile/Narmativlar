from django.db.models import Q
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
    success_url = reverse_lazy("student-list")


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "course/course_form.html"
    success_url = reverse_lazy("course-list")


class CourseDeleteView(DeleteView):
    model = Course
    template_name = "course/course_confirm_delete.html"
    success_url = reverse_lazy("course-list")


from django.db.models import Q
from django.views.generic import ListView

from .models import Student, Course


class StudentListView(ListView):
    model = Student
    template_name = "student/student_list.html"
    context_object_name = "students"

    paginate_by = 5

    def get_queryset(self):

        students = Student.objects.all()

        search = self.request.GET.get("search")
        course = self.request.GET.get("course")

        # SEARCH
        if search:
            students = students.filter(
                Q(full_name__icontains=search) |
                Q(email__icontains=search)
            )

        # FILTER
        if course:
            students = students.filter(course_id=course)

        return students

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["courses"] = Course.objects.all()

        return context


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
