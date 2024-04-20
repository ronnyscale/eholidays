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
    path("search/", views.search, name="search"),
    path("holiday/<str:slug>/", views.holiday_detail, name="holiday_detail"),
    path(
        "day/<int:year>/<int:month>/<int:day>/", views.day_holidays, name="day_holidays"
    ),
]
