from django.shortcuts import render, redirect
from referrals.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.


def my_recommendation_view(request):
    profile = Profile.objects.get(user=request.user)

    my_recs = profile.get_recommened_profiles()

    return render(request, "profile.html", {"my_recs": my_recs})


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
            registered_profile.recommended_by = recommeneded_by_profile.user

            registered_profile.save()
        else:
            form.save()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")

        user = authenticate(request, username=username, password=password)

        login(request, user)
        return redirect("main")

    return render(request, "signup.html", {"form": form})


def main_view(request, *args, **kwargs):
    code = kwargs.get("ref_code")
    try:
        profile = Profile.objects.get(code=code)
        # store the profile id in the sessions variable ref_profile
        request.session["ref_profile"] = profile.id

    except:
        pass
    return render(request, "main.html")
