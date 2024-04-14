# calendar_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "hashtag/<slug:hashtag>/",
        views.get_holidays_by_hashtag,
        name="holidays_by_hashtag",
    ),
]
