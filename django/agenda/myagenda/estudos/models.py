from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Materia(models.Model):
    nome = models.CharField(max_length=200)
    data_criacao = models.DateTimeField('date published')
    grau_conhecimento =  models.IntegerField(default=0) 
    tamanho = models.IntegerField(default=0)
    grau_dificuldade =  models.IntegerField(default=0)
    topicos = models.IntegerField(default=0)
    peso = models.IntegerField(default=0)
    percentual = models.FloatField()
    aproveitamento = models.FloatField()
    
    def __str__(self):
        return self.nome


class Topico(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    peso = models.IntegerField(default=0)
    aproveitamento = models.IntegerField(default=0)
    
    def __str__(self):
        return self.descricao