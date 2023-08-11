from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.utils.translation import gettext_lazy as _
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from .constants import LANGUAGES, TOPICS
from .models import AudioFile, Hymn, Topic, Language, Author, Arranger, Transcriber, Translator

class AudioFileInLine(admin.TabularInline):
    model = AudioFile
    extra = 0

@admin.register(Hymn)
class HymnAdmin(admin.ModelAdmin):
    exclude = ['slug']
    inlines = [AudioFileInLine]
    list_display = ['title', 'get_topics', 'language', 'release_date']
    list_filter = [('topics', RelatedDropdownFilter), ('language', RelatedDropdownFilter),'release_date']
    list_per_page = 10
    search_fields = ['title__istartswith']
    autocomplete_fields = ['topics', 'authors', 'arrangers', 'transcribers', 'translators', 'language']

    @admin.display(description=_('topics'))    
    def get_topics(self, hymn: Hymn):
        return "\n".join([str(t) + ', ' for t in hymn.topics.all()])
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('language').prefetch_related('topics', 'audio_files')

    
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['code', 'hymns_count']
    list_per_page = 10
    search_fields = ['code']

    @admin.display(ordering='hymns_count', description=_('hymns count'))
    def hymns_count(self, topic: Topic):
        url = (
            reverse('admin:hymnbook_hymn_changelist')
            + '?'
            + urlencode({
                'topic__code': str(topic.code)
            })
            )
        return format_html('<a href="{}">{}</a>', url, topic.hymns_count)
    
    def get_queryset(self, request):
        q=''

        try:
            q = request.GET['q']
            copy = request.GET.__copy__()
            copy.__delitem__('q')
            request.GET = copy
            
        except:
            pass
        
        result_list = []

        for i in TOPICS:
            if q in i[1].lower():
                result_list.append(f'{i[0]}')

        return super().get_queryset(request).annotate(
            hymns_count=Count('hymns')
        ).filter(code__in=result_list)
    
    def get_search_results(self, request, queryset, search_term):
        if not any(search_term):
            return queryset, False

        result_list = []
        for i in TOPICS:
            if search_term in i[1].lower():
                result_list.append(f'{i[0]}')

        return queryset.filter(code__in=result_list), False

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['code', 'hymns_count']
    list_per_page = 10
    search_fields = ['code']

    @admin.display(ordering='hymns_count', description=_('hymns count'))
    def hymns_count(self, language: Language):
        url = (
            reverse('admin:hymnbook_hymn_changelist')
            + '?'
            + urlencode({
                'language__code': str(language.code)
            })
            )
        return format_html('<a href="{}">{}</a>', url, language.hymns_count)

    def get_queryset(self, request):
        q=''

        try:
            q = request.GET['q']
            copy = request.GET.__copy__()
            copy.__delitem__('q')
            request.GET = copy
            
        except:
            pass
        
        result_list = []

        for i in LANGUAGES:
            if q in i[1].lower():
                result_list.append(f'{i[0]}')

        return super().get_queryset(request).annotate(
            hymns_count=Count('hymns')
        ).filter(code__in=result_list)
    
    def get_search_results(self, request, queryset, search_term):
        if not any(search_term):
            return queryset, False

        result_list = []
        for i in LANGUAGES:
            if search_term in i[1].lower():
                result_list.append(f'{i[0]}')

        return queryset.filter(code__in=result_list), False

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'hymns_count']
    list_per_page = 10
    search_fields = ['first_name__icontains', 'last_name__icontains']

    @admin.display(ordering='hymns_count', description=_('hymns count'))
    def hymns_count(self, author: Author):
        url = (
            reverse('admin:hymnbook_hymn_changelist')
            + '?'
            + urlencode({
                'author__id': str(author.id)
            })
            )
        return format_html('<a href="{}">{}</a>', url, author.hymns_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            hymns_count=Count('hymns')
        )
    
@admin.register(Arranger)
class ArrangerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'hymns_count']
    list_per_page = 10
    search_fields = ['first_name__icontains', 'last_name__icontains']

    @admin.display(ordering='hymns_count', description=_('hymns count'))
    def hymns_count(self, arranger: Arranger):
        url = (
            reverse('admin:hymnbook_hymn_changelist')
            + '?'
            + urlencode({
                'arranger__id': str(arranger.id)
            })
            )
        return format_html('<a href="{}">{}</a>', url, arranger.hymns_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            hymns_count=Count('hymns')
        )
    
@admin.register(Transcriber)
class TranscriberAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'hymns_count']
    list_per_page = 10
    search_fields = ['first_name__icontains', 'last_name__icontains']

    @admin.display(ordering='hymns_count', description=_('hymns count'))
    def hymns_count(self, transcriber: Transcriber):
        url = (
            reverse('admin:hymnbook_hymn_changelist')
            + '?'
            + urlencode({
                'transcriber__id': str(transcriber.id)
            })
            )
        return format_html('<a href="{}">{}</a>', url, transcriber.hymns_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            hymns_count=Count('hymns')
        )

@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'hymns_count']
    list_per_page = 10
    search_fields = ['first_name__icontains', 'last_name__icontains']

    @admin.display(ordering='hymns_count', description=_('hymns count'))
    def hymns_count(self, translator: Translator):
        url = (
            reverse('admin:hymnbook_hymn_changelist')
            + '?'
            + urlencode({
                'translator__id': str(translator.id)
            })
            )
        return format_html('<a href="{}">{}</a>', url, translator.hymns_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            hymns_count=Count('hymns')
        )