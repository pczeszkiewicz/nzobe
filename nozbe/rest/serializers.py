from rest_framework import serializers

from nozbe.models import Title, Name


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('id', 'primary_title', 'original_title', 'start_year', 'genres')


class NameSerializer(serializers.ModelSerializer):
    known_for_titles = TitleSerializer(many=True, read_only=True)

    class Meta:
        model = Name
        fields = ('id', 'primary_name', 'known_for_titles')
