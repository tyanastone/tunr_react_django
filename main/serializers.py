from rest_framework import serializers
from .models import Song, Artist


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'preview_url', 'artist')


class ArtistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'photo_url', 'nationality', 'songs')
