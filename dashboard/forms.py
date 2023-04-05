from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']

# This is used to make the due field accept date format in database
class DateInput(forms.DateInput):
    input_type= 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject','title','description','due','is_finished']



class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter your search : ")


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']



class UserRegistrationForm(UserCreationForm):
    
    email = forms.CharField(max_length=254, required=True,  widget=forms.EmailInput())
    class Meta:
    
        model = User
        fields = ['username','email' ,'password1', 'password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data