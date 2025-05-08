from rest_framework import viewsets
from ..models import BEPEC
from api.api.serializers import BEPECSerializer

class BEPECViewSet(viewsets.ModelViewSet):
    queryset = BEPEC.objects.all()
    serializer_class = BEPECSerializer
