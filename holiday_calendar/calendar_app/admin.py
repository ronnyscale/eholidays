from django.contrib import admin
from .models import Holiday, Category, Location, Hashtag


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "category", "location"]
    list_editable = [
        "date",
        "category",
        "location",
    ]  # Поля, которые можно редактировать из списка записей
    list_filter = ["date", "category", "location"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ["name"]
