from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    matricula = models.IntegerField()
    curso = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    nome_do_professor = models.TextField(max_length=255)
    codigo = models.IntegerField()
    disciplina = models.TextField(max_length=255)

