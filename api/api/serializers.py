from rest_framework import serializers
from api.models import Classe, Matiere, Chapitre, Devoir, Document, BEPEC

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ['id', 'nom', 'author']

class MatiereSerializer(serializers.ModelSerializer):
    classe = ClasseSerializer()
    
    class Meta:
        model = Matiere
        fields = ['id', 'nom', 'classe', 'author']

class ChapitreSerializer(serializers.ModelSerializer):
    matiere = MatiereSerializer()
    
    class Meta:
        model = Chapitre
        fields = ['id', 'titre', 'matiere', 'fichier_pdf', 'author']

class DevoirSerializer(serializers.ModelSerializer):
    matiere = MatiereSerializer()
    classe = ClasseSerializer()
    enseignant = serializers.StringRelatedField()

    class Meta:
        model = Devoir
        fields = ['id', 'titre', 'description', 'matiere', 'fichier_pdf', 'date', 'annee', 'classe', 'categorie', 'enseignant']

class DocumentSerializer(serializers.ModelSerializer):
    classe = ClasseSerializer()
    author = serializers.StringRelatedField()

    class Meta:
        model = Document
        fields = ['id', 'titre', 'description', 'fichier_pdf', 'categorie', 'date', 'classe', 'author']

class BEPECSerializer(serializers.ModelSerializer):
    matière = MatiereSerializer()
    classe = ClasseSerializer()

    class Meta:
        model = BEPEC
        fields = ['id', 'nom', 'date', 'matière', 'classe', 'description']
