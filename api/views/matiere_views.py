from rest_framework import viewsets
from api.filters import MatiereFilter
from ..models import Matiere
from api.api.serializers import MatiereSerializer
from django_filters.rest_framework import DjangoFilterBackend


class MatiereViewSet(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MatiereFilter
