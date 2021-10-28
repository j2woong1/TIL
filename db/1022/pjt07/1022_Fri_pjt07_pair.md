1022_Fri_pjt07_pair

```
초기세팅
$ python -m venv venv
$ activate / ctr+shi+p > Enter interpreter path... > find > venv > Script > python.exe선택
$ pip install django django-extensions ipython
$ pip install django django-extensions ipython django-bootstrap-v5
$ django-admin startproject pjt07 .
accounts는 베이스코드 복붙
$ python manage.py startapp community

----------
settings.py

INSTALLED_APPS = [
    'accounts',
    'community',
    'django-extensions',
    'bootstrap5',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
----
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
------

```

