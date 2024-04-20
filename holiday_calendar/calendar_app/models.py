from django.utils.text import slugify
from unidecode import unidecode  # Импортируем функцию unidecode для транслитерации
from django.db import models
from django.db import IntegrityError
import uuid


class Hashtag(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Хэштег")
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Транслитерация и создание слага для хештега
        slug_base = slugify(unidecode(self.name))
        self.slug = slug_base
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория", null=True, blank=True
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Местоположение", null=True, blank=True
    )

    def __str__(self):
        return self.name


class Holiday(models.Model):
    name = models.CharField(max_length=100, verbose_name="Праздник")
    date = models.DateField(verbose_name="Дата")
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )  # Связь с моделью Category
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, verbose_name="Местоположение"
    )  # Связь с моделью Location
    hashtags = models.ManyToManyField(Hashtag, verbose_name="Хэштеги")
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Транслитерация и создание слага для хештега
        slug_base = slugify(unidecode(self.name))
        self.slug = slug_base
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
