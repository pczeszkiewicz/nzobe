from rest_framework import viewsets

from nozbe.models import Title, Name
from nozbe.rest.serializers import TitleSerializer, NameSerializer


class TitleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows create SafeFile
    """
    queryset = Title.objects.order_by('primary_title')
    serializer_class = TitleSerializer
    filter_fields = ('start_year',)

    def get_queryset(self):
        queryset = super().get_queryset()
        genres = self.request.GET.get('genres')
        if genres:
            queryset = queryset.filter(genres__icontains=genres)
        return queryset


class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer
    filter_fields = ('primary_name',)
