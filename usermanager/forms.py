from django.forms import ModelForm
from django.contrib import messages
from django import forms
from .models import *

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

class UserForm(forms.ModelForm):
    g = [("Male", "Male"), ("Female", "Female")]
    p = [("self", "self"), ("Relative", "Relative"), ("Brother", "Brother"), ("Sister","sister"), ("Son","Son"), ("Daughter","Daughter"), ("Friend","Friend"), ("Marriage Buerau", "Marriage Buerau")]
    year = [str(i) for i in range(1980, 2010)]
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter Email"}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter Phone Number"}))
    password = forms.CharField(label='Create Password', max_length=10, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter Password"}))
    gender = forms.ChoiceField(label="Gender :", choices=g)
    dob = forms.DateField(label="Select Date Of Birth :", widget=forms.SelectDateWidget(years=year))
    profilefor = forms.ChoiceField(label="Profile For :", choices=p)
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter Height(in ft)"}))
    weight = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter Weight(in kg)"}))
    color = forms.ChoiceField(label="Skin Color :", choices=[("Dark","Dark"),("Fair", "Fair"),("Moderate", "Moderate")])
    religion = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Religion: Hindu/Muslim/Sikh etc."}))
    caste = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Caste"}))
    status = forms.ChoiceField(label="Marital Status :", choices=[("Never Married","Never Married"),("Widowed", "Widowed"),("Divorced", "Divorced"), ("Awaiting Divorce", "Awaiting Divorce")])
    disability = forms.ChoiceField(label="Any Disability :", choices=[("None","None"),("Physically Challenged","Physically Challenged" )])
    familystatus = forms.ChoiceField(label="Family Status :", choices=[("Middle Class","Middle Class"),("Affluent","Affluent"),("Upper Middle Class","Upper Middle Class"), ("Rich","Rich")])
    familytype = forms.ChoiceField(label="Family Type :", choices=[("Joint","Joint"),("Nuclear","Nuclear")])
    familyvalue = forms.ChoiceField(label="Family Value :", choices=[("Orthodox","Orthodox"),("Traditional","Traditional"),("Moderate","Moderate"), ("Liberal","Liberal")])
    qualification = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Qualification: "}))
    diet = forms.ChoiceField(label="Diet :", choices=[("Vegetarian","Vegetarian"),("Non Vegetarian","Non Vegetarian")])
    work = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Work"}))
    income = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter Annual Income "}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter Age: "}))
    class Meta:
        model = User
        fields = '__all__'
