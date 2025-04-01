from rest_framework import serializers
from api.models import Classe, Matiere, Chapitre, Devoir, Document, BEPEC, Corrige, CorrigeBEPEC

class ClasseSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Classe
        fields = ['id', 'nom', 'author']

class MatiereSerializer(serializers.ModelSerializer):
    classes = ClasseSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Matiere
        fields = ['id', 'nom', 'classes', 'author']

class ChapitreSerializer(serializers.ModelSerializer):
    matiere = serializers.PrimaryKeyRelatedField(queryset=Matiere.objects.all())
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Chapitre
        fields = ['id', 'titre', 'matiere', 'fichier_pdf', 'author']

class DevoirSerializer(serializers.ModelSerializer):
    matiere = serializers.PrimaryKeyRelatedField(queryset=Matiere.objects.all())
    classe = serializers.PrimaryKeyRelatedField(queryset=Classe.objects.all())
    enseignant = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Devoir
        fields = ['id', 'titre', 'description', 'matiere', 'fichier_pdf', 'date', 'annee', 'classe', 'categorie', 'enseignant']

class CorrigeSerializer(serializers.ModelSerializer):
    devoir = serializers.PrimaryKeyRelatedField(queryset=Devoir.objects.all())
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Corrige
        fields = ['id', 'titre', 'description', 'fichier_pdf', 'devoir', 'author']

class BEPECSerializer(serializers.ModelSerializer):
    matiere = serializers.PrimaryKeyRelatedField(queryset=Matiere.objects.all())
    classe = serializers.PrimaryKeyRelatedField(queryset=Classe.objects.all())

    class Meta:
        model = BEPEC
        fields = ['id', 'nom', 'date', 'annee_examen', 'matiere', 'classe', 'description']

class CorrigeBEPECSerializer(serializers.ModelSerializer):
    bepec = serializers.PrimaryKeyRelatedField(queryset=BEPEC.objects.all())
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CorrigeBEPEC
        fields = ['id', 'titre', 'description', 'fichier_pdf', 'bepec', 'author']

class DocumentSerializer(serializers.ModelSerializer):
    classe = serializers.PrimaryKeyRelatedField(queryset=Classe.objects.all())
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'titre', 'description', 'fichier_pdf', 'categorie', 'date', 'classe', 'author']
