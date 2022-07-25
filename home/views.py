from django.http import HttpResponse
from django.shortcuts import redirect, render
from authentication.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_index(request):
    print(request.user)
    if not request.user.is_authenticated:
        return render(request, "home_index.html")
    else:
        user_id = request.user.id
        usertype = Profile.objects.filter(user = User.objects.get(id=user_id)).values('type')[0]['type']
        return redirect("home:dashboard",usertype)

@login_required
def dashboard(request,type):
    user_id = request.user.id
    user = User.objects.get(id = request.user.id)
    profile = Profile.objects.filter(user = User.objects.get(id=user_id)).all().values()
    return render(request, 'dashboard.html', {'info': profile, 'user': user})