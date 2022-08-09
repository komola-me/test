from django import views
from django.urls import include, path
from rest_framework import routers
from posts import views
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


router = routers.DefaultRouter()
router.register(r'api/v1/post', views.PostViewSet)
router.register(r'api/v1/categories', views.CategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]