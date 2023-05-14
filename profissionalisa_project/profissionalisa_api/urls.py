from django.urls import include, path

from rest_framework import routers

from profissionalisa_api.views import UsuariosViewSet, VideosViewSet, MentoresViewSet, CursosViewSet, ComentariosViewSet, SessoesViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'videos', VideosViewSet)
router.register(r'mentores', MentoresViewSet)
router.register(r'cursos', CursosViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'sessoes', SessoesViewSet)



urlpatterns = [
    path('',include(router.urls)),
]