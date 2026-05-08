from django import forms
from .models import Course, Student


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if not phone.startswith("+998"):
            raise forms.ValidationError(
                "Telefon raqam +998 bilan boshlanishi kerak"
            )

        if len(phone) < 13:
            raise forms.ValidationError(
                "Telefon raqam kamida 13 ta belgidan iborat bo‘lishi kerak"
            )

        return phone


    def clean_email(self):
        email = self.cleaned_data.get("email")

        if "@" not in email:
            raise forms.ValidationError(
                "Email ichida @ bo‘lishi kerak"
            )

        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")

        if len(full_name) < 3:
            raise forms.ValidationError(
                "Full name kamida 3 ta belgidan iborat bo‘lishi kerak"
            )

        return full_name