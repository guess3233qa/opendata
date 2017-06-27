from django.conf.urls import include, url
from .views import here , menu
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^poll/$', menu),
    url(r'^abc/$', include('poll.urls'))
]
