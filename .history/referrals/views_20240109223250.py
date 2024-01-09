from django.shortcuts import render
from referrals.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.


def signup_view(request):
    return render(request, "signup.html")


def main_view(request, *args, **kwargs):
    code = kwargs.get("ref_code")
    try:
        profile = Profile.objects.get(code=code)
        request.session["ref_profile"] = profile.id
    except:
        pass
    return render(request, "main.html")
