from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models

TITLE_MAX_GENRES = getattr(settings, 'NOZBE_TITLE_MAX_GENRES', 3)
NAME_MAX_PRIMARY_PROFESSIONS = getattr(settings, 'NOZBE_NAME_MAX_PRIMARY_PROFESSIONS', 3)


class Title(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=16)
    title_type = models.CharField(max_length=100)
    primary_title = models.CharField(max_length=500)
    original_title = models.CharField(max_length=500)
    is_adult = models.BooleanField()
    start_year = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)
    runtime_minutes = models.PositiveIntegerField(null=True, blank=True)
    genres = ArrayField(models.CharField(max_length=64), null=True, db_index=True, size=TITLE_MAX_GENRES)


class Name(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=16)
    primary_name = models.CharField(max_length=500, db_index=True)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    death_year = models.PositiveIntegerField(null=True, blank=True)
    primary_profession = ArrayField(models.CharField(max_length=64), null=True, size=NAME_MAX_PRIMARY_PROFESSIONS)
    known_for_titles = models.ManyToManyField('nozbe.Title')
