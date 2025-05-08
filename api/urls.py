from rest_framework.routers import DefaultRouter
from .views.classe_views import ClasseViewSet
from .views.matiere_views import MatiereViewSet
from .views.chapitre_views import ChapitreViewSet
from .views.devoir_views import DevoirViewSet
from .views.document_views import DocumentViewSet
from .views.bepec_views import BEPECViewSet
from .views.corrige_views import CorrigeViewSet, CorrigeBEPECViewSet

router = DefaultRouter()
router.register(r'classes', ClasseViewSet)
router.register(r'matieres', MatiereViewSet)
router.register(r'chapitres', ChapitreViewSet)
router.register(r'devoirs', DevoirViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'bepecs', BEPECViewSet)
router.register(r'corriges', CorrigeViewSet)
router.register(r'corriges-bepec', CorrigeBEPECViewSet)

urlpatterns = router.urls
