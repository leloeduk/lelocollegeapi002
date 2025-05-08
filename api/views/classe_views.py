from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Classe
from api.api.serializers import ClasseSerializer
from ..filters import ClasseFilter

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.prefetch_related(
        'matieres__chapitres', 'matieres__author', 'author'
    )
    serializer_class = ClasseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClasseFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            queryset = queryset.only('id', 'nom', 'author')
        return queryset

    @action(detail=False, methods=['get'], url_path='6eme')
    def classe_6eme(self, request):
        return self.retrieve_specific_classe('6eme')

    @action(detail=False, methods=['get'], url_path='5eme')
    def classe_5eme(self, request):
        return self.retrieve_specific_classe('5eme')

    def retrieve_specific_classe(self, nom_classe):
        try:
            instance = self.get_queryset().get(nom=nom_classe)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Classe.DoesNotExist:
            return Response({'detail': 'Classe non trouvée'}, status=404)
