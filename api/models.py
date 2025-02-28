from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Importer le modèle User de Django

class Classe(models.Model):
    nom = models.CharField(max_length=50)
    author = models.ForeignKey(User, related_name='classes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Matiere(models.Model):
    nom = models.CharField(max_length=50)
    classe = models.ForeignKey(Classe, related_name='matieres', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='matieres', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} ({self.classe.nom})'

class Chapitre(models.Model):
    titre = models.CharField(max_length=100)
    matiere = models.ForeignKey(Matiere, related_name='chapitres', on_delete=models.CASCADE)
    fichier_pdf = models.FileField(upload_to='chapitres_pdfs/')
    author = models.ForeignKey(User, related_name='chapitres', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titre} ({self.matiere.nom})'

class Devoir(models.Model):
    CATEGORIES = [
        ('classe', 'Devoir de classe'),
        ('departemental', 'Devoir départemental'),
        ('composition', 'Composition'),
    ]

    titre = models.CharField(max_length=100)
    description = models.TextField()
    matiere = models.ForeignKey(Matiere, related_name='devoirs', on_delete=models.CASCADE)
    fichier_pdf = models.FileField(upload_to='devoirs_pdfs/')
    date = models.DateField()
    annee = models.CharField(max_length=4)  # Ajout du champ pour l'année
    classe = models.ForeignKey(Classe, related_name='devoirs', on_delete=models.CASCADE)  # Lien vers la classe
    categorie = models.CharField(choices=CATEGORIES, max_length=20)  # Ajout du champ pour la catégorie
    enseignant = models.ForeignKey(User, related_name='devoirs_composes', on_delete=models.CASCADE)  # Ajout du champ pour l'enseignant

    def __str__(self):
        return f'{self.titre} ({self.matiere.nom})'

class Document(models.Model):
    CATEGORIES = [
        ('guides', 'Guides'),
        ('livres', 'Livres au programme'),
        ('pedagogiques', 'Fichiers pédagogiques'),
        ('autres', 'Autres'),
    ]
    
    titre = models.CharField(max_length=100)
    description = models.TextField()
    fichier_pdf = models.FileField(upload_to='documents_pdfs/')
    categorie = models.CharField(choices=CATEGORIES, max_length=20)
    date = models.DateField()
    classe = models.ForeignKey(Classe, related_name='documents', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='documents', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titre} - {self.categorie} ({self.classe.nom})'


class BEPEC(models.Model):
    nom = models.CharField(max_length=200)  # Nom du BEPEC
    date = models.DateField()  # Date de l'examen
    matière = models.ForeignKey(Matiere, on_delete=models.CASCADE)  # Lien vers la matière
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)  # Lien vers la classe
    description = models.TextField(blank=True, null=True)  # Description de l'examen BEPEC

    def __str__(self):
        return f"{self.nom} - {self.matière.nom} - {self.classe.nom}"
