from django.conf.urls import url, include
from django.contrib import admin

api_urlpatterns = [
    url('', include('apps.ship.urls'))
]


urlpatterns = api_urlpatterns + [
    url(r'^admin/', admin.site.urls)
]
