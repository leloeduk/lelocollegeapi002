from django.db import models
from django.contrib.auth.models import User

class Classe(models.Model):
    nom = models.CharField(max_length=50)
    author = models.ForeignKey(User, related_name='classes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Matiere(models.Model):
    nom = models.CharField(max_length=50)
    classes = models.ManyToManyField(Classe, related_name='matieres')
    author = models.ForeignKey(User, related_name='matieres', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

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
    annee = models.CharField(max_length=4)
    classe = models.ForeignKey(Classe, related_name='devoirs', on_delete=models.CASCADE)
    categorie = models.CharField(choices=CATEGORIES, max_length=20)
    enseignant = models.ForeignKey(User, related_name='devoirs_composes', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titre} ({self.matiere.nom})'

class Corrige(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    fichier_pdf = models.FileField(upload_to='corriges_pdfs/')
    devoir = models.ForeignKey(Devoir, related_name='corriges', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='corriges', on_delete=models.CASCADE)

    def __str__(self):
        return f'Corrigé de {self.devoir.titre}'

class BEPEC(models.Model):
    nom = models.CharField(max_length=200)
    date = models.DateField()
    annee_examen = models.CharField(max_length=4)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - {self.matiere.nom} - {self.classe.nom} ({self.annee_examen})"

class CorrigeBEPEC(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    fichier_pdf = models.FileField(upload_to='corriges_bepec_pdfs/')
    bepec = models.ForeignKey(BEPEC, related_name='corriges', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='corriges_bepec', on_delete=models.CASCADE)

    def __str__(self):
        return f'Corrigé de {self.bepec.nom}'

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

class Corrige(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    fichier_pdf = models.FileField(upload_to='corriges_pdfs/')
    devoir = models.ForeignKey(Devoir, related_name='corriges', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='corriges', on_delete=models.CASCADE)

    def __str__(self):
        return f'Corrigé de {self.devoir.titre}'

class CorrigeBEPEC(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    fichier_pdf = models.FileField(upload_to='corriges_bepec_pdfs/')
    bepec = models.ForeignKey(BEPEC, related_name='corriges', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='corriges_bepec', on_delete=models.CASCADE)

    def __str__(self):
        return f'Corrigé de {self.bepec.nom}'