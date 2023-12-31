"""
URL configuration for mcec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

admin.site.site_header = 'Orfeones MCEC Administration'
admin.site.index_title = _('Home')
admin.site.site_title = _('MCEC Management')

urlpatterns = i18n_patterns(
    path('mcec/administration/', admin.site.urls),
    #path("__debug__/", include("debug_toolbar.urls")),
    path('hymnbook/', include('hymnbook.urls')),
    path('members/', include('members.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    prefix_default_language=False
)
