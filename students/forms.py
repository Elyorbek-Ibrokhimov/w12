from django import forms
from .models import Maktab, Sinf, Student

class MaktabForm(forms.ModelForm):
    class Meta:
        model = Maktab
        fields = ['nomi']

class SinfForm(forms.ModelForm):
    class Meta:
        model = Sinf
        fields = ['nomi', 'maktab']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['nomi', 'sinf']
