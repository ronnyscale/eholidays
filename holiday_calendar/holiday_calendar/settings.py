"""
Django settings for holiday_calendar project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1v1qz6+_va#xgy(f2y=o_x)(a6+#z=^c4l+9_g-rm%4v-pg9v-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "calendar_app",
    
    "bootstrap4",
    "admin_interface",
    "colorfield",
    
    "django.contrib.humanize",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'holiday_calendar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'holiday_calendar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "eholiday",
        "USER": "eholiday_admin",
        "PASSWORD": "adminsfu",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = "Asia/Krasnoyarsk"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMIN_INTERFACE_CONFIG = {
    "SEARCH_URL": "http://google.com/search?q=",  # Настройка поиска, можно оставить пустым
    "CONFIGS": {
        "skin": "skin-blue",  # Цветовая схема. Доступные значения: skin-blue, skin-black, skin-red, skin-yellow, skin-purple, skin-green
        "layout": "vertical",  # Вертикальный или горизонтальный интерфейс. Доступные значения: vertical, horizontal
        "boxed": False,  # Установите в True, чтобы иметь ограниченную область содержимого
        "collapsed": False,  # Свернуть боковую панель
        "sidebar": {
            "nav_small_text": False,  # Уменьшить текст в навигационной боковой панели
            "show_user_apps": False,  # Показать приложения пользователя,  # Скрыть навигацию по боковой панели
        },
        "navbar": {
            "fixed": True,  # Фиксированная панель навигации сверху
            "show_apps": True,  # Показать приложения
        },
        "breadcrumbs": {
            "fixed": True,  # Фиксированные хлебные крошки
            "autohide": False,  # Автоматически скрывать хлебные крошки на мобильных устройствах
        },
        "footer": {
            "fixed": True,  # Фиксированный подвал
        },
        "show_about": False,  # Показать сведения о проекте
        "show_settings": True,  # Показать настройки
        "show_language": False,  # Показать выбор языка
        "show_theme": True,  # Показать выбор темы
        "show_sidebar": True,  # Показать переключатель боковой панели
        "show_navbar": True,  # Показать переключатель панели навигации
        "show_breadcrumbs": True,  # Показать переключатель хлебных крошек
        "show_footer": True,  # Показать переключатель подвала
    },
}
