from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('article', ArticleViewSet)

urlpatterns = [
    # path('user_count/', user_count_view),
    path('', include(router.urls)),
]
