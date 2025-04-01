from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClasseViewSet, MatiereViewSet, ChapitreViewSet, DevoirViewSet, DocumentViewSet, BEPECViewSet, CorrigeViewSet ,CorrigeBEPECViewSet

router = DefaultRouter()
router.register(r'classes', ClasseViewSet)
router.register(r'matieres', MatiereViewSet)
router.register(r'chapitres', ChapitreViewSet)
router.register(r'devoirs', DevoirViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'bepecs', BEPECViewSet)
router.register(r'corriges', CorrigeViewSet)
router.register(r'corriges_bepec', CorrigeBEPECViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
