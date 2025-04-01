from django.contrib import admin
from .models import Classe, Matiere, Chapitre, Devoir, Document, BEPEC, Corrige, CorrigeBEPEC

class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'author')
    search_fields = ('nom',)

class MatiereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'author')
    search_fields = ('nom',)


class CorrigeAdmin(admin.ModelAdmin):
    list_display = ('titre', 'devoir', 'author')
    search_fields = ('titre', 'devoir__titre', 'author__username')
    list_filter = ('devoir', 'author')

class ChapitreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'matiere', 'author')
    search_fields = ('titre', 'matiere__nom')

class DevoirAdmin(admin.ModelAdmin):
    list_display = ('titre', 'matiere', 'classe', 'enseignant', 'date')
    search_fields = ('titre', 'matiere__nom', 'classe__nom', 'enseignant__username')
    list_filter = ('categorie', 'date')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'classe', 'author', 'date')
    search_fields = ('titre', 'classe__nom', 'author__username')
    list_filter = ('categorie', 'date')

class BEPECAdmin(admin.ModelAdmin):
    list_display = ('nom', 'matiere', 'classe', 'annee_examen', 'date')
    search_fields = ('nom', 'matiere__nom', 'classe__nom', 'annee_examen')

class CorrigeBEPECAdmin(admin.ModelAdmin):
    list_display = ('titre', 'bepec', 'author')
    search_fields = ('titre', 'bepec__nom', 'author__username')
    list_filter = ('bepec', 'author')




admin.site.register(CorrigeBEPEC, CorrigeBEPECAdmin)
admin.site.register(Corrige, CorrigeAdmin)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Matiere, MatiereAdmin)
admin.site.register(Chapitre, ChapitreAdmin)
admin.site.register(Devoir, DevoirAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(BEPEC, BEPECAdmin)
