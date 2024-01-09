from django.urls import path

from . import views


urlpatterns = [
    path("", views.main_view, name="main"),
    path("<str:ref_code>/", views.main_view, name="main"),
]
