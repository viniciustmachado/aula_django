from django.db import models

# Create your models here.
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(null=False) # não aceita nulo
    telefone = models.TextField(null=True) # aceita nulo
 