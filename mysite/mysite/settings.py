"""
Django settings for mysite project.
"""

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_NAME = "DJ4E Projects"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5-cmh1m7&opk@m-vib&bvzl_7j&6pfdym^vu$%x2b0fznvov3r"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_extensions",  # Extensions - see requirements.txt
    "crispy_forms",
    "crispy_bootstrap5",
    "social_django",
    "django.contrib.admindocs",
    "taggit",
    # Home application
    "home.apps.HomeConfig",
    # Other apps
    "ads.apps.AdsConfig",
    "autos.apps.AutosConfig",
    "cats.apps.CatsConfig",
    "hello.apps.HelloConfig",
    "polls.apps.PollsConfig",
]

# For crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "home.context_processors.settings",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# For local
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# For PythonAnywhere
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'amog98$ads',
#         'USER': 'amog98',
#         'PASSWORD': 'MWWU9w@mkZxk#^'
#         'HOST': 'amog98.mysql.pythonanywhere-services.com',
#          'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configure the social login
try:
    from . import github_settings

    SOCIAL_AUTH_GITHUB_KEY = github_settings.SOCIAL_AUTH_GITHUB_KEY
    SOCIAL_AUTH_GITHUB_SECRET = github_settings.SOCIAL_AUTH_GITHUB_SECRET
except:
    print(
        "When you want to use social login, please see dj4e-samples/github_settings-dist.py"
    )

# https://python-social-auth.readthedocs.io/en/latest/configuration/django.html#authentication-backends
# https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html
AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

LOGOUT_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = "/"

# Needed for 3.2 and later
# https://stackoverflow.com/questions/67783120/warning-auto-created-primary-key-used-when-not-defining-a-primary-key-type-by
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# https://coderwall.com/p/uzhyca/quickly-setup-sql-query-logging-django
# https://stackoverflow.com/questions/12027545/determine-if-django-is-running-under-the-development-server
