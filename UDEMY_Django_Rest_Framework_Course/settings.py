"""
Section 2 Notes:

1. API - Application Programming Interface
         Middleman, connecting 2 different applications(e.g.: Uber and Google Maps)
         Types of API:
            - Private - (within organization, e.g.: app for web, ios, mac at the same time)
            - Partner - (business, design content for business partners, groups, e.g.: prime video
                        takes the video ratings from IMDB)
            - Public - (when everyone is allowed to register as user, any third party app e.g.: register,
                        free and paid servide to utilize, OpenWeather)
         We use JSON or XML to get response
         Consumers vs. Providers
         Understanding URLs - Base Url + Endpoint

2. REST API - architecture which follows some patterns for everything
        Endpoint(e.g.: /movies/127/reviews)
        Methods(send requests and receive response)
            - C - Create - POST    (e.g.: add a new movie)
            - R - Read   - GET     (e.g.: list an individual movie or many as a list)
            - U - Update - PUT     (e.g.: update movie)
            - D - Delete - DELETE  (e.g.: delete movie)
        Headers - (e.g.: status code - 200 OK ; 201 Created)
        Data/Body - follow JSON to send all kind of data


Section 3 Notes:

1.When we work with JSON:
    - We do not have a single quote - only double ("")
    - When we have a boolean it is written lowercase (true/false)

Section 4 Notes:

1. Installation:
    - pip install djangorestframework
    - add 'rest_framework' to INSTALLED_APPS
    - add path('api-auth/', include('rest_framework.urls')) to urls.py

2.Theory:
    - Serialization:    Model Objects --> Python Dictionary --> JSON Data
    - De-serialization: JSON Data     --> Python Dictionary --> Model Objects
    - Types of Serializers:
            - serializer.Serializer
            - serializer.ModelSerializer
    - Types of Views:
            - CBV - import APIView (class) (e.g.: class ListUser(APIView))
                  - Generic views
                  - Mixins
                  - Concrete View Classes
                  - ViewSets
            - FBV - utilize decorator @api_view (e.g.: @api_view(http_method_names=['GET'])
    - Working with API - accessing it:
            - DRF Browsable API
            - Postman
            - HTTPie

Section 5 Notes:

1. Validations they are called when we call 'serializer.is_valid()':
    - field level - only checking a particular field
    - object level - e.g.: movie name should not be the same as description
    - validators - add validator in field

2. Relationships:
    - One-To-One   -  one single obj can be tied up to only 1 obj (one restaurant can have only 1 location)
                      restaurant=models.OneToOneFiled(Place, on_delete=models.CASCADE, primary_key=True)
    - One-To-Many  -  Netflix can have many movies, but 1movie can have only 1 streaming platform
                      reporter=models.ForeignKey(Reporter, on_delete=models.CASCADE)
    - Many-To-Many - one article can be published on many publications, and one publication can have many articles
                      publications = models.ManyToManyField(Publication)

3. class VideoSerializer(serializers.HyperlinkedModelSerializer)
    serializer = VideoSerializer(queryset, context={'request': request})

4. Generic Views
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^2_8glmeypx=i8lp92&odd*q&()*6v2+cs3r@x=emqg!p!qti4'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'watchlist_app',

    'rest_framework',
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

ROOT_URLCONF = 'UDEMY_Django_Rest_Framework_Course.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'UDEMY_Django_Rest_Framework_Course.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
