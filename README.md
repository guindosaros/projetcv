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

## Application Riz

```python 
#Pour tous ceux Parle du Riz les varietes de chiffre les chiffres et autres 
  
  from django.db import models
  from tinymce import HTMLField
  
   class Bienfait(models.Model):
    titre = models.CharField(max_length=255)
    description =  models.TextField()
    images = models.FileField(upload_to='Article')
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
  
   class Meta:
        verbose_name = "Bienfait"
        verbose_name_plural = "Bienfaits"

    def __str__(self):
        return self.titre
  
  
  class Suffisances(models.Model):
    titre = models.CharField(max_length=255)
    description =  models.TextField()
    
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
  
   class Meta:
        verbose_name = "Suffisance"
        verbose_name_plural = "Suffisances"

    def __str__(self):
        return self.titre
  
  class SuffisancesImage(models.Model):
    suffisance = models.ForeignKey(Suffisances, on_delete=models.CASCADE, related_name='suf_image')
    images = models.FileField(upload_to='SuffisancesImage') 
   
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
  
   class Meta:
        verbose_name = "SuffisancesImage"
        verbose_name_plural = "SuffisancesImage"

    def __str__(self):
        pass
  
  ```
  ## Application Contact
  ```python
  from django.db import models
  
  class Message(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    objet = models.CharField(max_length=50)
    contenue = models.TextField()

    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True,null=True)
    date_upd = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.email

  ```
  
    ## Application mprsite
  
