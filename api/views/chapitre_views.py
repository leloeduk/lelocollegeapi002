from rest_framework import viewsets
from ..models import Chapitre
from api.api.serializers import ChapitreSerializer
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import ChapitreFilter

class ChapitreViewSet(viewsets.ModelViewSet):
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChapitreFilter
