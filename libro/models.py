from django.db import models

class Autor(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,blank = False,null=False)
    apellidos=models.CharField(max_length=100,blank = False,null=False)
    nacionalidad=models.CharField(max_length=50,blank = False,null=False)
    descripcion=models.TextField(blank = False,null=False)
