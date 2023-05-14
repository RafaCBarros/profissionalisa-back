# from django.shortcuts import render
from rest_framework import viewsets

from profissionalisa_api.serializers import UsuariosSerializer, VideosSerializer, MentoresSerializer, CursosSerializer, ComentariosSerializer, SessoesSerializer
from profissionalisa_api.models import Usuario, Video, Mentor, Curso, Comentario, Sessao

# Create your views here.
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer
class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideosSerializer
class MentoresViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentoresSerializer
class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursosSerializer
class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer
class SessoesViewSet(viewsets.ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessoesSerializer