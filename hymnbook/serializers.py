from rest_framework import serializers
from .models import Hymn, AudioFile, Author, Arranger, Transcriber, Translator

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ['id', 'voice_type', 'audio_file']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']

class ArrangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arranger
        fields = ['id', 'first_name', 'last_name']

class TranscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcriber
        fields = ['id', 'first_name', 'last_name']

class TranslatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translator
        fields = ['id', 'first_name', 'last_name']
    
class HymnListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hymn
        fields = ['slug', 'title', 'release_date', 'pdf_file', 'topics', 'audio_files']

class HymnDetailSerializer(serializers.ModelSerializer):
    audio_files = AudioSerializer(many=True)
    authors = AuthorSerializer(many=True)
    arrangers = ArrangerSerializer(many=True)
    transcribers = TranslatorSerializer(many=True)
    translators = TranslatorSerializer(many=True)

    class Meta:
        model = Hymn
        fields = ['slug', 'title', 'release_date', 'pdf_file', 'notes', 'authors', 'arrangers', 'transcribers', 'translators', 'topics', 'audio_files']
        lookup_field: ['slug']