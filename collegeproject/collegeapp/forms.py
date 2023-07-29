from django import forms
from .models import  *
from django.forms import widgets

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'dob', 'age', 'gender', 'number', 'email', 'address', 'course', 'department', 'purpose', 'Notebook', 'Pen', 'Exam_papers']
    
        widgets = {
            'name': forms.TextInput(),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.NumberInput(),
            'gender': forms.Select(choices=GENDER, attrs={
                        'style': 'background:none; border:none; width:100%; outline:none; padding:2%;',
                    }),
            'number': forms.TextInput(),
            'email': forms.EmailInput(),
            'address': forms.TextInput(),
            'department': forms.Select(attrs={
                    'style': 'background:none; border:none; width:100%; outline:none; padding:2%;',
                    'onchange' : "getcourses(this);"
                    }),
            'course': forms.Select(attrs={
                    'style': 'background:none; border:none; width:100%; outline:none; padding:2%;', 
                    }),
            'purpose': forms.Select(choices=PURPOSE, attrs={
                        'style': 'background:none; border:none; width:100%; outline:none; padding:2%;',
                    }),
            'Notebook': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Pen': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'Exam_papers': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }