from rest_framework import serializers

from nozbe.models import Title, Name


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('id', 'primary_title', 'original_title', 'start_year', 'genres')


class KnownForTitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('primary_title',)


class NameSerializer(serializers.ModelSerializer):
    known_for_titles = KnownForTitlesSerializer(many=True, read_only=True)

    class Meta:
        model = Name
        fields = ('id', 'primary_name', 'known_for_titles')
