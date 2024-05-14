from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    fone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.fone}"
