from django.urls import path
from user.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', UserViewSet, basename='user')
router.register(r'<int:id>', UserViewSet, basename='user')

urlpatterns = router.urls