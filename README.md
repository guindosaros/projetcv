# projetcv

vera.jolie@icloud.com
Maman2019

# Propostion de models Projet Mpr 

## Application Mistére 

```python 
  from django.db import models
  from tinymce import HTMLField
  
  class Presentation(models.Model):
    titre = models.CharField(max_length=255)
    description =  HTMLField('description')
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
          verbose_name = "Presentation"
          verbose_name_plural = "Presentations"

     def __str__(self):
          return self.titre
    
  class Details(models.Model):
    titre = models.CharField(max_length=255)
    image = models.FileField(upload_to='details/')
    description =  HTMLField('description')
   
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
          verbose_name = "Detail"
          verbose_name_plural = "Details"

      def __str__(self):
          return self.titre
  
   class MotsMinistre(models.Model):
    titre = models.CharField(max_length=255)
    photo = models.FileField(upload_to='Mots/')
    description =  HTMLField('description')
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
     class Meta:
          verbose_name = "Mots du Ministre"
          verbose_name_plural = "Mots du Ministre"

      def __str__(self):
          return self.titre


    class Ministre(models.Model):
      nom = models.CharField(max_length=255)
      photo = models.FileField(upload_to='ministre/')
      description =  HTMLField('description')
      facebook = models.URLField()
      twitter = models.URLField()

      status = models.BooleanField(default=True)
      date_add = models.DateTimeField(auto_now_add=True)
      date_upd = models.DateTimeField(auto_now=True)

      class Meta:
          verbose_name = "Ministre"
          verbose_name_plural = "Ministres"

      def __str__(self):
          return self.nom
  

```
## Application Actualite
from django.db import models
from django.utils.text import slugify
import hashlib
from tinymce import HTMLField

```python
  class Article(models.Model):
    titre = models.TextField()
    description =  HTMLField('description')
    images = models.FileField(upload_to='Article')
    slug = models.SlugField(editable=False, unique=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        encoded_id = self.id
        self.slug = slugify(self.titre.replace(" ", "-") + ' ' + str(encoded_id))
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.titre


```

