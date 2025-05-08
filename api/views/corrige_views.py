from rest_framework import viewsets
from ..models import Corrige, CorrigeBEPEC
from api.api.serializers import CorrigeSerializer, CorrigeBEPECSerializer

class CorrigeViewSet(viewsets.ModelViewSet):
    queryset = Corrige.objects.all()
    serializer_class = CorrigeSerializer

class CorrigeBEPECViewSet(viewsets.ModelViewSet):
    queryset = CorrigeBEPEC.objects.all()
    serializer_class = CorrigeBEPECSerializer
