import django_filters
from .models import Classe, Matiere, Chapitre, Devoir, Document, BEPEC, Corrige, CorrigeBEPEC

class ClasseFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Classe
        fields = ['nom', 'author']

class MatiereFilter(django_filters.FilterSet):
    # Filtre personnalisé pour la relation ManyToMany
    classe = django_filters.ModelChoiceFilter(
        field_name='classes',  # Notez le pluriel 'classes' qui correspond au ManyToManyField
        queryset=Classe.objects.all(),
        label="Classe"
    )
    
    class Meta:
        model = Matiere
        fields = ['nom']  # Ne gardez que les champs directs du modèle Matiere

class ChapitreFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Chapitre
        fields = ['titre', 'matiere']

# Ajoute d'autres filtres si nécessaire pour les autres modèles
