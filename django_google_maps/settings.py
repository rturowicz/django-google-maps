from django.conf import settings


GOOGLE_MAPS_JS_URL = getattr(settings, 'GOOGLE_MAPS_JS_URL', settings.STATIC_URL + 'django_google_maps/js')
GOOGLE_MAPS_CSS_URL = getattr(settings, 'GOOGLE_MAPS_CSS_URL', settings.STATIC_URL + 'django_google_maps/css')
GOOGLE_MAPS_JQUERY_URL = getattr(settings, 'GOOGLE_MAPS_JQUERY_URL', 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4')
