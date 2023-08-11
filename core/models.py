from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False, help_text=_('Designates whether the user identity has been verified'), verbose_name=_('verified'))

class CarouselSlide(models.Model):
    title = models.CharField(max_length=100, help_text=_('Carousel slide title'), verbose_name=_('slide title'))
    text = models.TextField(help_text=_('Carousel slide description'), verbose_name=_('slide description'))
    background_image_file = models.ImageField(default='default.jpg', upload_to='images/slides_images/', help_text=_('Carousel slide background image'), verbose_name=_('slide background image'))

    class Meta:
        verbose_name = _('carousel slide')
        verbose_name_plural = _('carousel slides')
