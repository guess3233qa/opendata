from django.conf.urls import include, url
from poll import views

urlpatterns = [
    url(r'^abc/$' , views.abc)
]
