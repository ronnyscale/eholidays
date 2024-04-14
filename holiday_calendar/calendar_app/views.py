from django.shortcuts import render
from django.http import JsonResponse
from .models import Holiday, Hashtag
from .forms import HolidayFilterForm
from datetime import datetime


def index(request):
    today = datetime.now().date()
    today_holidays = Holiday.objects.filter(date=today)
    num_today_holidays = today_holidays.count()

    # Форма фильтрации
    if request.method == "GET":
        form = HolidayFilterForm(request.GET)
        if form.is_valid():
            category = form.cleaned_data.get("category")
            location = form.cleaned_data.get("location")
            if category:
                today_holidays = today_holidays.filter(
                    category__name=category
                )  # Фильтруем по имени категории
            if location:
                today_holidays = today_holidays.filter(location=location)
    else:
        form = HolidayFilterForm()

    return render(
        request,
        "calendar_app/index.html",
        {
            "today_holidays": today_holidays,
            "num_today_holidays": num_today_holidays,
            "form": form,  # Передаем форму фильтрации в шаблон
        },
    )


def get_holidays_by_hashtag(request, hashtag):
    try:
        # Ищем хештег по транслитерированному имени
        hashtag_obj = Hashtag.objects.get(slug=hashtag)
        # Получаем все праздники, связанные с данным хештегом
        holidays = Holiday.objects.filter(hashtags=hashtag_obj)
        return render(
            request, "calendar_app/holidays_by_hashtag.html", {"holidays": holidays, "hashtag": hashtag_obj.name}
        )
    except Hashtag.DoesNotExist:
        return render(
            request,
            "calendar_app/holidays_by_hashtag.html",
            {"error_message": "Хештег не найден"},
        )
