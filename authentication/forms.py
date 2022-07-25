from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class DoctorSignupForm(UserCreationForm):
    type = forms.CharField(widget=forms.HiddenInput(), initial="Doctor")
    profile_photo = forms.ImageField(allow_empty_file=False, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    city = forms.CharField(max_length=20, required=True)
    state = forms.CharField(max_length=20, required=True)
    pincode = forms.CharField(max_length=7, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name','profile_photo', 'username', 'email', 'password1', 'password2', 'address', 'city', 'state', 'pincode')
        labels = {'address': "Address Line", 'city': 'City', 'state': "State", "pincode": 'Pincode', 'type': 't'}

class PatientSignupForm(UserCreationForm):
    type = forms.CharField(widget=forms.HiddenInput(), initial="Patient")
    profile_photo = forms.ImageField(allow_empty_file=False, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    city = forms.CharField(max_length=20, required=True)
    state = forms.CharField(max_length=20, required=True)
    pincode = forms.CharField(max_length=7, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name','profile_photo', 'username', 'email', 'password1', 'password2', 'address', 'city', 'state', 'pincode')
        labels = {'address': "Address Line", 'city': 'City', 'state': "State", "pincode": 'Pincode'}