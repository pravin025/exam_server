
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import UserView

router = DefaultRouter()
router.register(r'user', UserView)


urlpatterns = [
    path('', include(router.urls))
    ]

