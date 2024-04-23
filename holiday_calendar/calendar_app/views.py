from datetime import datetime

from django.shortcuts import render
from django.db.models import Q
from django.db.models.functions import Lower

from django.utils import timezone
from .models import Holiday, Hashtag, Category, Location


def search(request):
    today = timezone.now().date()
    q = request.GET.get("query")

    holidays_today = Holiday.objects.filter(date=today)
    all_holidays = Holiday.objects.all()

    categories = Category.objects.all()
    locations = Location.objects.all()

    category = request.GET.get("category")
    location = request.GET.get("location")

    selected_holidays = holidays_today

    if category and category != "":
        selected_holidays = all_holidays.filter(category=category)

    if location and location != "":
        selected_holidays = selected_holidays.filter(location=location)

    if q:
        # Выполняем поиск по имени и описанию праздника
        holidays = Holiday.objects.filter(
            Q(name__iregex=q) | Q(description__iregex=q)
        )
        return render(
            request,
            "calendar_app/search_results.html",
            {
                "search_results": holidays,
                "today": today,
                "categories": categories,
                "locations": locations,
                "selected_category": int(category) if category else None,
                "selected_location": int(location) if location else None,
            },
        )
    else:
        return render(
            request, "calendar_app/search_results.html", {"search_results": []}
        )


def index(request):
    today = timezone.now().date()
    holidays_today = Holiday.objects.filter(date=today)
    all_holidays = Holiday.objects.all()

    categories = Category.objects.all()
    locations = Location.objects.all()

    category = request.GET.get("category")
    location = request.GET.get("location")

    selected_holidays = holidays_today

    if category and category != "":
        selected_holidays = all_holidays.filter(category=category)

    if location and location != "":
        selected_holidays = selected_holidays.filter(location=location)

    return render(
        request,
        "calendar_app/index.html",
        {
            "today": today,
            "selected_holidays": selected_holidays,
            "categories": categories,
            "locations": locations,
            "selected_category": int(category) if category else None,
            "selected_location": int(location) if location else None,
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


def holiday_detail(request, slug):
    holiday = Holiday.objects.get(slug=slug)
    return render(request, "calendar_app/holiday_detail.html", {"holiday": holiday})


def day_holidays(request, year, month, day):
    russian_months = {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря",
    }

    selected_date = datetime(int(year), int(month), int(day))
    formatted_date = f"{selected_date.day} {russian_months[selected_date.month]} {selected_date.year} года"

    # Фильтруем праздники по выбранной дате
    holidays = Holiday.objects.filter(date__month=int(month), date__day=int(day))

    context = {"holidays": holidays, "selected_day": formatted_date}
    return render(request, "calendar_app/day_holidays.html", context)
