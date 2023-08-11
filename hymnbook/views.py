from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from .filters import HymnFilter
from .models import Hymn
from .serializers import HymnListSerializer, HymnDetailSerializer

class HymnViewSet(ReadOnlyModelViewSet):
    queryset = Hymn.objects.all()
    serializer_class = HymnListSerializer
    filterset_class = HymnFilter
    ordering_fields = ['title', 'release_date']
    search_fields = ['title']
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'
    
    def retrieve(self, request, slug=None):
        queryset = Hymn.objects.select_related('language').prefetch_related('authors', 'arrangers', 'transcribers', 'translators', 'audio_files').all()
        hymn = get_object_or_404(queryset, slug=slug)
        serializer = HymnDetailSerializer(hymn, context={'request': request})
        return Response(serializer.data)
