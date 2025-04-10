from rest_framework import viewsets
from .models import Classe, Matiere, Chapitre, Devoir, Document, BEPEC ,Corrige, CorrigeBEPEC
from api.api.serializers import ClasseSerializer, MatiereSerializer, ChapitreSerializer, DevoirSerializer, DocumentSerializer, BEPECSerializer, CorrigeSerializer, CorrigeBEPECSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class MatiereViewSet(viewsets.ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer

class ChapitreViewSet(viewsets.ModelViewSet):
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer

class DevoirViewSet(viewsets.ModelViewSet):
    queryset = Devoir.objects.all()
    serializer_class = DevoirSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class BEPECViewSet(viewsets.ModelViewSet):
    queryset = BEPEC.objects.all()
    serializer_class = BEPECSerializer

class CorrigeViewSet(viewsets.ModelViewSet):
    queryset = Corrige.objects.all()
    serializer_class = CorrigeSerializer


class CorrigeBEPECViewSet(viewsets.ModelViewSet):
    queryset = CorrigeBEPEC.objects.all()
    serializer_class = CorrigeBEPECSerializer