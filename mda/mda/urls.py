
from django.conf.urls import url, include
# from django.contrib.auth import get_user_model
from rest_framework import routers
from django.urls import include, path
from user.views import UserViewSet


router = routers.DefaultRouter(trailing_slash=True)
router.register(r'user', UserViewSet, base_name='user')



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]

