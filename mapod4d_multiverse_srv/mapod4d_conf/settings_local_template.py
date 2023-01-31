import mapod4d_multiverse_srv.mains_settings


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-chu)o2r8t##wbz7br#=x+vyfi30qt&o4@gs#3ia+9x+q0h77qe'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mapod4d_mult_srv',
        'USER': 'mapod4d_mult_u',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

MAPOD4D = {
   'multiverse': {
       'name': 'test',
    },
}

