from django.db import models
from django.conf import settings
from django.utils.text import slugify
from .constants import LANGUAGES, AUDIO_VOICE_TYPES, TOPICS
from django.utils.translation import gettext_lazy as _

class Topic(models.Model):        
    code = models.CharField(max_length=3, choices=TOPICS, default='ADO', primary_key=True, verbose_name=_('topic'))
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['code']
        verbose_name = _('topic')
        verbose_name_plural = _('topics')

    def __str__(self):
        for i in TOPICS:
            if self.code == i[0]:
                return f'{i[1]}'
        return f'{self.code}'
    
class Language(models.Model):        
    code = models.CharField(max_length=2, choices=LANGUAGES, default='es', primary_key=True, verbose_name=_('language'))
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['code']
        verbose_name = _('language')
        verbose_name_plural = _('languages')

    def __str__(self):
        for i in LANGUAGES:
            if self.code == i[0]:
                return f'{i[1]}'   
        return f'{self.code}'

class Author(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_('first name'))
    last_name = models.CharField(max_length=255, verbose_name=_('last name'))
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Arranger(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_('first name'))
    last_name = models.CharField(max_length=255, verbose_name=_('last name'))
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('arranger')
        verbose_name_plural = _('arrangers')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Transcriber(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_('first name'))
    last_name = models.CharField(max_length=255, verbose_name=_('last name'))
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('transcriber')
        verbose_name_plural = _('transcribers')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Translator(models.Model):
    first_name = models.CharField(max_length=255, verbose_name=_('first name'))
    last_name = models.CharField(max_length=255, verbose_name=_('last name'))
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('translator')
        verbose_name_plural = _('translators')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Hymn(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    slug = models.SlugField(max_length=255, blank=True)
    topics = models.ManyToManyField(Topic, related_name='hymns', verbose_name=_('topics'))
    authors = models.ManyToManyField(Author, related_name='hymns', blank=True, verbose_name=_('authors'))
    arrangers = models.ManyToManyField(Arranger, related_name='hymns', blank=True, verbose_name=_('arrangers'))
    transcribers = models.ManyToManyField(Transcriber, related_name='hymns',blank=True, verbose_name=_('transcribers'))
    translators = models.ManyToManyField(Translator, related_name='hymns', blank=True, verbose_name=_('traslators'))
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name='hymns', verbose_name=_('language'))
    release_date = models.DateField(help_text=_('Hymn release date'), verbose_name=_('release date'))
    pdf_file = models.FileField(upload_to='hymnbook/pdf-files/', verbose_name=_('pdf file'))
    notes = models.TextField(null=True, blank=True, verbose_name=_('notes'))
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = _('hymn')
        verbose_name_plural = _('hymns')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Hymn, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

class AudioFile(models.Model):
    hymn = models.ForeignKey(Hymn, on_delete=models.CASCADE, related_name='audio_files')
    voice_type = models.CharField(max_length=2, choices=AUDIO_VOICE_TYPES, default='S0', verbose_name=_('voice type'))
    audio_file = models.FileField(upload_to='hymnbook/audio-files/', verbose_name=_('audio file'))

    class Meta:
        verbose_name = _('audio file')
        verbose_name_plural = _('audio files')

    def __str__(self):
        return f'{self.voice_type}'

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookmarks')
    hymn = models.ForeignKey(Hymn, on_delete=models.CASCADE, related_name='bookmarks')

    class Meta:
        verbose_name = _('bookmark')
        verbose_name_plural = _('bookmarks')