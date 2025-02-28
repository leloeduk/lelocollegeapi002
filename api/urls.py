from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClasseViewSet, MatiereViewSet, ChapitreViewSet, DevoirViewSet, DocumentViewSet, BEPECViewSet

router = DefaultRouter()
router.register(r'classes', ClasseViewSet)
router.register(r'matieres', MatiereViewSet)
router.register(r'chapitres', ChapitreViewSet)
router.register(r'devoirs', DevoirViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'bepecs', BEPECViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
