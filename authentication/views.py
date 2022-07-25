from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Profile
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def auth_signup(request):
    if request.method == "POST":
        return HttpResponse("Method not allowed")
    else:
        doctorform = DoctorSignupForm()
        patientform = PatientSignupForm()
    return render(request, "auth_signup.html", {'doctorform': doctorform, "patientform": patientform})

def update_user_data(user, form):
    p = Profile(user = user, address=form.cleaned_data.get('address'), type=form.cleaned_data.get('type'), profile_photo = form.cleaned_data.get('profile_photo'), city = form.cleaned_data.get('city'), state = form.cleaned_data.get('state'), pincode=form.cleaned_data.get('pincode'))
    p.save()


def SaveRegisterForm(request):
    if request.method == 'POST':
        if request.POST.get("type") == "Doctor":
            form = DoctorSignupForm(request.POST, request.FILES)
        else:
            form = PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            update_user_data(user, form)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home:home_index')
        else:
            print("Error")
            print(form.errors)
    else:
        return HttpResponse("Method Not Allowed")

def logout_view(request):
    logout(request)
    return redirect('home:home_index')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('username'))
            user = authenticate(username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                # A backend authenticated the credentials
                return redirect("home:home_index")
            else:
            # No backend authenticated the credentials        
                return redirect("auth:login_view")
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'auth_login.html', {'form': form})