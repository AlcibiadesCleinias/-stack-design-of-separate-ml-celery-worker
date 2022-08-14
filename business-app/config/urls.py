from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from polls.views import *

API_PREFIX = 'api/v1/'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start-ml/', start_ml),
    path('result-ml/<str:task>', result_ml)
]


if len(urlpatterns) > 1 and settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
