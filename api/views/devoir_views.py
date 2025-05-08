from rest_framework import viewsets
from ..models import Devoir
from api.api.serializers import DevoirSerializer

class DevoirViewSet(viewsets.ModelViewSet):
    queryset = Devoir.objects.all()
    serializer_class = DevoirSerializer
