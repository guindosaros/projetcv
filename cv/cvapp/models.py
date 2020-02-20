from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    photo = models.ImageField(upload_to='profile/photo')
    specialite = models.CharField(max_length=2250)
    adresse = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    numero = models.CharField(max_length=250)
    facebook = models.CharField(max_length=2250)
    github = models.CharField(max_length=2250)
    lindkedin = models.CharField(max_length=2250)
    

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user_profile.save()
    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        

class Details(models.Model):
    presentation = models.CharField(max_length=2250)
    description  = models.TextField()
    image = models.ImageField(upload_to='profile/photo')
    cv = models.FileField()
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.presentation

    class Meta:
        verbose_name = 'Details'
        verbose_name_plural = 'Detailss'


      
class About(models.Model):
    titre = models.CharField(max_length=250)
    description = HTMLField('Description')
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
        


class Specialite(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE,related_name='About_specialite')
    nom = models.CharField(max_length=250)
    icone = models.CharField(max_length=250)
    classe = models.CharField(max_length=250)
    animate = models.CharField(max_length=250)
    
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
 
    class Meta:
        
         verbose_name = 'Specialité'
         verbose_name_plural = 'Specialités'
         
         
class Education(models.Model):
    diplome = models.CharField(max_length=250)
    description = HTMLField('Description')
    slug = models.SlugField(unique=True)
        
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return self.diplome
    
    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'


class Competence(models.Model):
    titre = models.CharField(max_length=250)
    description = HTMLField('Description')
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = 'Competence'
        verbose_name_plural = 'Competences'
        

class DetailCompetence(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE,related_name='competebce_details',null=True)
    nom = models.CharField(max_length=250)
    pourcentage = models.IntegerField()
    classe = models.CharField(max_length=250)
    animate = models.CharField(max_length=250)
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'DetailCompetence'
        verbose_name_plural = 'DetailCompetences'
        
        
class Experience(models.Model):
    nom = models.CharField(max_length=250)
    annee = models.CharField(max_length=250)
    description = HTMLField('Description')
    icone = models.CharField(max_length=250)
    classe = models.CharField(max_length=250)
    animate = models.CharField(max_length=250)
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom

    class Meta:
        
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
  
  
        
class Service(models.Model):
    nom = models.CharField(max_length=250)
    description = HTMLField('Description')
    icone = models.CharField(max_length=250)
    classe = models.CharField(max_length=250)
    animate = models.CharField(max_length=250)
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.nom

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        
        
class Message(models.Model):
    nom = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    sujet = models.CharField(max_length=250)
    message = models.TextField()
    
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'