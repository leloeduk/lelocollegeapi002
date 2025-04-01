from rest_framework import serializers
from api.models import Classe, Matiere, Chapitre, Devoir, Document, BEPEC, Corrige, CorrigeBEPEC

class ChapitreSerializer(serializers.ModelSerializer):
    # Le champ fichier_pdf est conservé tel quel, en respectant la clé du modèle
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Chapitre
        fields = ['id', 'titre', 'fichier_pdf', 'author']
        
class MatiereSerializer(serializers.ModelSerializer):
    # On imbrique les chapitres en utilisant le related_name 'chapitres' défini dans le modèle Chapitre
    chapitres = ChapitreSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Matiere
        # Ici, on renvoie id, nom, la liste imbriquée des chapitres et l'auteur
        fields = ['id', 'nom', 'chapitres', 'author']
        
class ClasseSerializer(serializers.ModelSerializer):
    # On imbrique les matières en utilisant le related_name 'matieres' défini dans le modèle Matiere (ManyToManyField)
    matieres = MatiereSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Classe
        fields = ['id', 'nom', 'matieres', 'author']
        
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
