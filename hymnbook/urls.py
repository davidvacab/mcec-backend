from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('hymns', views.HymnViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

