from django.db import models

# Create your models here.
class Item(models.Model):
    nome_aluno = models.CharField(max_length= 200) #CharField se refere ao tipo de atributo que nesse caso é Char
    item = models.CharField(max_length= 200)
