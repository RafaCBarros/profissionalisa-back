from rest_framework import serializers

from profissionalisa_api.models import Usuario, Video, Mentor, Curso, Comentario, Sessao

class UsuariosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'data_nascimento','email','telefone','login','senha']
class MentoresSerializer (serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['nome','sobrenome','email','telefone']
class CursosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['nome','mentor']
class VideosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['nome','duracao','media_nota','video_url','curso']
class ComentariosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['usuario','curso','conteudo','data_envio']
class SessoesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sessao
        fields = ['usuario','video','tempo_assistido','nota']