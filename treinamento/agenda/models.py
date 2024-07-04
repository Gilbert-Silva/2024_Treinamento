from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    fone = models.CharField(max_length=15)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.nome} - {self.email} - {self.fone}"

class Servico(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()
    duracao = models.IntegerField()  # Duração em minutos, por exemplo

    def __str__(self):
        return f"{self.descricao} - {self.valor:.2f} - {self.duracao}"

