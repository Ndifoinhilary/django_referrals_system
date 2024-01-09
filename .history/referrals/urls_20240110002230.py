from django.urls import path

from . import views


urlpatterns = [
    path("", views.main_view, name="main"),
    path("profiles/", views.my_recommendation_view, name="profiles"),
    path("signup/", views.signup_view, name="signup"),
    path("<str:ref_code>/", views.main_view, name="main"),
]
