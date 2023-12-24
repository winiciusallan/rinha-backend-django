from django.db import models


class Pessoa(models.Model):
    id = models.BigAutoField(primary_key=True)
    apelido = models.CharField(max_length=32)
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    stacka = models.JSONField(blank=True)

