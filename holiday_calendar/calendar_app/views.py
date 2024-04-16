from django.shortcuts import render
from django.utils import timezone
from .models import Holiday, Hashtag, Category, Location


from django.utils import timezone


def index(request):
    today = timezone.now().date()
    holidays_today = Holiday.objects.filter(date=today)
    all_holidays = Holiday.objects.all()

    categories = Category.objects.all()
    locations = Location.objects.all()

    category = request.GET.get("category")
    location = request.GET.get("location")

    selected_holidays = (
        holidays_today  # Показывать только праздники сегодняшнего дня по умолчанию
    )

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
