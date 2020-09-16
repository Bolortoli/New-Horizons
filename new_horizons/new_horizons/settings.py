# Cpanel or Local Environment?
DEV_ENV = 'local'

import os
from . import config as configs
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#oq%0lf4!6s)x(e#xswmhq04)#&1w-4!#ny-u0#*l8s74oyfx@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEV_ENV == 'cpanel' :
  ALLOWED_HOSTS = ["newhorizons.mn","www.newhorizons.mn",'localhost', '127.0.0.1']
else :
  ALLOWED_HOSTS = ["*"]
  
# Application definition

INSTALLED_APPS = [
    'ckeditor',
    'django_ckeditor_5',
    'jet.dashboard',
    'jet',
    'admin_honeypot',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_reorder',
    'horizonapp',
    'rosetta',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'new_horizons.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'horizonapp.context_processors.global_settings',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'new_horizons.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

prefix_default_language=False

LANGUAGE_CODE = 'en'
LANGUAGES = (
      ('en',_('English')),
      ('mn',_('Mongolia')),
    )


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'uploads/'

if DEV_ENV == 'cpanel' :
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    STATIC_ROOT = "/home/newhoriz/public_html/static/"
    MEDIA_ROOT = "/home/newhoriz/public_html/media/"
else :
    print('local')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'assets')
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  
  
  
  
  

# EMAIL_HOST = configs.EMAIL_HOST
# EMAIL_PORT = configs.EMAIL_PORT
# EMAIL_HOST_USER = configs.EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = configs.EMAIL_HOST_PASSWORD
# EMAIL_USE_TLS = configs.EMAIL_USE_TLS

# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_SECONDS = 1
# # SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_REFERRER_POLICY = 'origin'

# Django-jet configs
# Doc --> https://jet.readthedocs.io/en/latest/config_file.html

JET_DEFAULT_THEME = 'light-gray'
JET_SIDE_MENU_COMPACT = True


JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# CkEditor 5 configs

customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ]

# CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote', 'imageUpload'
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', 'imageTitle', '|', 'imageStyle:alignLeft', 'imageStyle:full',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    }
}

# Admin reorder

ADMIN_REORDER = [
    {
        'app': 'horizonapp', 'label': 'Мэдээ',
            'models': (
                'horizonapp.News',
                'horizonapp.NewsCategory'
            )
    },
    {
        'app': 'horizonapp', 'label': 'Түрээслэгчийн мэдээллүүд',
            'models': (
                'horizonapp.BuildingRents',
            )
    },
    {
        'app': 'horizonapp', 'label': 'Тохиргоо',
            'models': (
                'horizonapp.PDFbrochure',
                'horizonapp.Settings',
                'horizonapp.ContactUs',
                'horizonapp.Three60Pic',
            )
    },
    {
        'app': 'horizonapp', 'label': 'Түрээслэгч',
            'models': (
                'horizonapp.Organization',
                'horizonapp.OrganizationCategory',
            )
    },
    {
        'app': 'horizonapp', 'label': 'Нүүр хуудас',
            'models': (
                'horizonapp.HomeSlider',
                'horizonapp.BuildingIntro',
                'horizonapp.FeatureCard',
                'horizonapp.FloorPlan',
                'horizonapp.ReasonBoxes',
            )
    },
        {
        'app': 'horizonapp', 'label': 'Дэд хуудас',
            'models': (
                'horizonapp.SubPage',
                'horizonapp.SubPages_NoTitleIcon_Rightpic',
                'horizonapp.SubPages_NoTitleIcon_Leftpic',
                'horizonapp.SubPages_TitleIcon',
                'horizonapp.SubPages_Slider',
            )
    },
]

# JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
#     {'label': 'Мэдээ мэдээлэл', 'app_label': 'horizonapp', 'items': [
#         {'name': 'NewsCategory', 'label': 'Мэдээний категори', 'url': 'http://newhorizons.mn/admin/horizonapp/newscategory/'},
#         {'name': 'News', 'label': 'Мэдээ', 'url': 'http://newhorizons.mn/admin/horizonapp/news/'},
#     ]},
#     {'label': 'Нүүр хуудас', 'app_label': 'horizonapp', 'items': [
#         {'name': 'HomeSlider', 'label': 'Нүүр хуудас слайдэр', 'url': 'http://newhorizons.mn/admin/horizonapp/homeslider/'},
#         {'name': 'BuildingIntro', 'label': 'Товч танилцуулга', 'url': 'http://newhorizons.mn/admin/horizonapp/buildingintro/'},
#         {'name': 'FeatureCard', 'label': '4 хайрцаг', 'url': 'http://newhorizons.mn/admin/horizonapp/featurecard/'},
#         {'name': 'FloorPlan', 'label': 'Давхарын план', 'url': 'http://newhorizons.mn/admin/horizonapp/FloorPlan/'},
#         {'name': 'ReasonBoxes', 'label': '7 шалтгаан', 'url': 'http://newhorizons.mn/admin/horizonapp/reasonboxes/'},
#         {'name': 'Three60Pic', 'label': '360 зураг', 'url': 'http://newhorizons.mn/admin/horizonapp/three60pic/'},
#     ]},
#     {'label': 'Түрээслэгч', 'app_label': 'horizonapp', 'items': [
#         {'name': 'OrganizationCategry', 'label': 'Байгууллагын төрөл', 'url': 'http://newhorizons.mn/admin/horizonapp/organization/'},
#         {'name': 'News', 'label': 'Байгууллага', 'url': 'http://newhorizons.mn/admin/horizonapp/organizationcategory/'},
#         {'name': 'BuildingRents', 'label': 'Түрээсийн мэдээлэл', 'url': 'http://newhorizons.mn/admin/horizonapp/buildingrents/'},
#     ]},
#     {'label': 'Бусад', 'app_label': 'horizonapp', 'items': [
#         {'name': 'PDFbrochure', 'label': 'PDF танилцуулга(линк)', 'url': 'http://newhorizons.mn/admin/horizonapp/pdfbrochure/'},
#         {'name': 'Settings', 'label': 'Вэб сайтын тохиргоо', 'url': 'http://newhorizons.mn/admin/horizonapp/settings/'},
#         {'name': 'ContactUs', 'label': 'Холбоо барих хүсэлтийн жагсаалт', 'url': 'http://newhorizons.mn/admin/horizonapp/contactus/'},
#     ]},
# ]

LOCALE_PATHS = (
      os.path.join(BASE_DIR,'locale/'),
    )
    
JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'
    
JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
JET_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'
JET_MODULE_YANDEX_METRIKA_CLIENT_ID = '301340f9eec946d6b527ead568dd1a9c'
JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET = '93dd8f0b36154e6ba31ac85ad9ce2b43'

JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'client_secret.json')
