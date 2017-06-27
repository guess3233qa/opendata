"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers, request
from api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Hauntedhouse',views.HViewSet)
router.register(r'Renthouses',views.RViewSet)
router.register(r'Firebrigade',views.FViewSet)
router.register(r'Policestation',views.PViewSet)
router.register(r'Cvs',views.CViewSet)
router.register(r'Excellentmarket',views.EViewSet)
router.register(r'Hardwareretail',views.HrtViewSet)
router.register(r'Hardwarestore',views.HstViewSet)
router.register(r'Restaurant',views.RestViewSet)
router.register(r'WChild',views.WViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/',include(router.urls))
]
