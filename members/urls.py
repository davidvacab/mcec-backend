from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProfileViewSet, ChurchViewSet

router = SimpleRouter()
router.register('profiles', ProfileViewSet)
router.register('churches', ChurchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
