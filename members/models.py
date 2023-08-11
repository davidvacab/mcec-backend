from django.db import models
from django.conf import settings
from .constants import PHONE_CODES, COUNTRY_NAMES, MEMBER_ROLES, MEMBER_VOICES
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255, verbose_name=_('first name'))
    last_name = models.CharField(max_length=255, verbose_name=_('last name'))
    bio = models.TextField(blank=True, default='Me', verbose_name=_('biography'))
    profile_picture = models.ImageField(default='members/default.jpg', upload_to='members/profile_pics/', blank=True, verbose_name=_('profile picture'))
    birthdate = models.DateField(verbose_name=_('birthdate'))
    phone_area_code = models.CharField(max_length=2, choices=PHONE_CODES, default="MX", verbose_name=_('phone country code'))
    phone_number = models.CharField(max_length=255, verbose_name=_('phone number'))
    voice_type = models.CharField(max_length=2, choices=MEMBER_VOICES, default='S1', verbose_name=_('voice type'))
    role = models.CharField(max_length=2, choices=MEMBER_ROLES, default='CM', help_text=_('Role in current choir'), verbose_name=_('choir role'))
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Church(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='church')
    minister_name = models.CharField(max_length=255, help_text=_('Name of current minister'), verbose_name=_('current minister name'))
    church_name = models.CharField(max_length=255, help_text=_('Name of church'), verbose_name=_('church name'))
    city = models.CharField(max_length=255, verbose_name=_('church city'))
    state = models.CharField(max_length=255, verbose_name=_('church state'))
    country = models.CharField(max_length=2, choices=COUNTRY_NAMES, default='mx', verbose_name=_('church country'))
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('church')
        verbose_name_plural = _('churches')

    def __str__(self):
        return f'{self.church_name}'