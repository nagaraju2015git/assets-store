from django.conf.urls import url
from . import views
from .views import UserViewSet, GroupViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    url(r'^assets/(?P<pk>[a-zA-Z0-9_-]+)/$', views.details),
    url(r'^assets/$', views.AssetList.as_view()),
    url(r'^assetsclass/$', views.AssetClassList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)