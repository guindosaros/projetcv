# projetcv

vera.jolie@icloud.com
Maman2019

# Propostion de models Projet Mpr 

## Application Mistére 

```python 
  from django.db import models
  from tinymce import HTMLField
  
  class Presenation(models.Model):
    titre = models.CharField(max_length=255)
    description =  HTMLField('description')
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    
  class Details(models.Model):
    titre = models.CharField(max_length=255)
    image = models.FileField(upload_to='details/')
    description =  HTMLField('description')
   
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

  
   class MotsMinistre(models.Model):
    titre = models.CharField(max_length=255)
    Photo = models.FileField(upload_to='Mots/')
    description =  HTMLField('description')
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
  
  class Ministre(models.Model):
    nom = models.CharField(max_length=255)
    Photo = models.FileField(upload_to='ministre/')
    description =  HTMLField('description')
    facebook = models.URLField()
    twitter = models.URLField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
  

```
