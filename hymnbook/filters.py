from django_filters import rest_framework as filters
from .models import Hymn

class HymnFilter(filters.FilterSet):
    class Meta:
        model = Hymn
        fields = {
            'title': ['icontains'],
            'topics': ['exact'],
            'language': ['exact'],
            'release_date': ['exact', 'year__gt', 'year__lt']
        }