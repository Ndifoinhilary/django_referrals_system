from django.shortcuts import render
from referrals.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.


def signup_view(request):
    profile_id = request.session.get("ref_profile")
    print("profile_id", profile_id)
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        if profile_id is not None:
            recommeneded_by_profile = Profile.objects.get(id=profile_id)

            instance = form.save()

            registered_user = User.objects.get(id=instance.id)
            registered_profile = Profile.objects.get(user=registered_user)
            registered_profile.recommended_by = recommeneded_by_profile

            registered_profile.save()
        else:
            form.save()

    return render(request, "signup.html")


def main_view(request, *args, **kwargs):
    code = kwargs.get("ref_code")
    try:
        profile = Profile.objects.get(code=code)
        # store the profile id in the sessions variable ref_profile
        request.session["ref_profile"] = profile.id

    except:
        pass
    return render(request, "main.html")
