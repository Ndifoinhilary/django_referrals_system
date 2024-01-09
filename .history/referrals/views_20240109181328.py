from django.shortcuts import render
from referrals.models import Profile

# Create your views here.


def main_view(request, *args, **kwargs):
    code = kwargs.get("ref_code")
    try:
        profile = Profile.objects.get(code=code)
        request.session["ref_code"] = profile.id
    except:
        pass
    return render(request, "main.html")
