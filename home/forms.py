from django import forms
from django.contrib.auth.models import User
from home.models import Contact, Profile

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['your_name', 'your_email', 'your_message']


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'phone', 'Class', 'Class_teacher', 'Admission_No' ]

        
