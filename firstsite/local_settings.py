
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'orangeblog_db',
#        'USER': 'admin',
#        'PASSWORD': 'adminadmin',
#        'HOST': 'localhost',
#        'PORT': '',
#    }
#}

