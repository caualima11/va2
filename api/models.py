from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    curso = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
