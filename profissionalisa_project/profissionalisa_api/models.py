import datetime
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=30),
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    # def save(self, *args, **kwargs):
    #    age = datetime.date.today()-self.data_nascimento #idade minima
    #    if (int((age).days/365.25) < 12):
    #        return
    #    else:
    #        super().save(*args, **kwargs)

class Mentor(models.Model):
    nome = models.CharField(max_length=30),
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nome
    
    #def save(self, *args, **kwargs):
    #    age = datetime.date.today()-self.data_nascimento # Idade minima
    #    if (int((age).days/365.25) < 18):
    #        return
    #    else:
    #        super().save(*args, **kwargs)

class Curso(models.Model):
    nome = models.CharField(max_length=30),
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    comentarios = models.ManyToManyField(Usuario, through="Comentario", through_fields=("curso","usuario"))
    
    def __str__(self):
        return self.nome

class Video(models.Model):
    nome = models.CharField(max_length=30),
    duracao = models.DurationField()
    media_nota = models.DecimalField(max_digits=4,decimal_places=2)
    video_url = models.URLField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    sessoes = models.ManyToManyField(Usuario, through="Sessao", through_fields=("video","usuario"))
    
    def __str__(self):
        return self.nome

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    conteudo = models.TextField(max_length=500)
    data_envio = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario} {self.video}"

class Sessao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    tempo_assistido = models.DurationField()
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return "{self.usuario} {self.video}"