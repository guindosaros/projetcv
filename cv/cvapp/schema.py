import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id
from . import models 
from django.contrib.auth.models import User

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        # Allow for some more advanced filtering here
        filter_fields = {
            # 'photo': ['exact'],
            'username': ['exact'],
        }
        interfaces = (relay.Node, )






class ProfileNode(DjangoObjectType):
    class Meta:
        model = models.Profile
        # Allow for some more advanced filtering here
        filter_fields = {
            # 'photo': ['exact'],
            'specialite': ['exact', 'icontains', 'istartswith'],
            'adresse': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
            'numero': ['exact', 'icontains', 'istartswith'],
            'github': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
            'user': ['exact'],
        }
        interfaces = (relay.Node, )
        
        
class DetailsNode(DjangoObjectType):
    class Meta:
        model = models.Details
        # Allow for some more advanced filtering here
        filter_fields = {
            'presentation': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            # 'image': ['exact'],
            # 'cv': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        

class AboutNode(DjangoObjectType):
    class Meta:
        model = models.About
        # Allow for some more advanced filtering here
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        
        
class SpecialiteNode(DjangoObjectType):
    class Meta:
        model = models.Specialite
        # Allow for some more advanced filtering here
        filter_fields = {
            'classe': ['exact', 'icontains', 'istartswith'],
            'nom': ['exact', 'icontains', 'istartswith'],
            'icone': ['exact', 'icontains', 'istartswith'],
            'nom': ['exact', 'icontains', 'istartswith'],
            'about': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        
        
        
class ServiceNode(DjangoObjectType):
    class Meta:
        model = models.Service
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'icone': ['exact', 'icontains', 'istartswith'],
            'classe': ['exact', 'icontains', 'istartswith'],
            'animate': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        
        
        
class EducationNode(DjangoObjectType):
    class Meta:
        model = models.Education
        # Allow for some more advanced filtering here
        filter_fields = {
            'diplome': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'slug': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        
        
        
        
        
        
class CompetenceNode(DjangoObjectType):
    class Meta:
        model = models.Competence
        # Allow for some more advanced filtering here
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        
        

        
class DetailCompetenceNode(DjangoObjectType):
    class Meta:
        model = models.DetailCompetence
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'pourcentage': ['exact', 'icontains', 'istartswith'],
            'classe': ['exact', 'icontains', 'istartswith'],
            'animate': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        
        

        
class ExperienceNode(DjangoObjectType):
    class Meta:
        model = models.Experience
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'annee': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'icone': ['exact', 'icontains', 'istartswith'],
            'classe': ['exact', 'icontains', 'istartswith'],
            'animate': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node,)
        
        
class MessageNode(DjangoObjectType):
    class Meta:
        model = models.Message
        # Allow for some more advanced filtering here
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
            'sujet': ['exact', 'icontains', 'istartswith'],
            'message': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
        interfaces = (relay.Node,)
                      
                      

class  Query(graphene.ObjectType):
    
    Profile = relay.Node.Field(ProfileNode)
    all_Profile = DjangoFilterConnectionField(ProfileNode)
    
    
    Details = relay.Node.Field(DetailsNode)
    all_Details = DjangoFilterConnectionField(DetailsNode)
    
    
    About = relay.Node.Field(AboutNode)
    all_About = DjangoFilterConnectionField(AboutNode)

    
    Specialite = relay.Node.Field(SpecialiteNode)
    all_Specialite = DjangoFilterConnectionField(SpecialiteNode)
    
    
    Service = relay.Node.Field(ServiceNode)
    all_Service = DjangoFilterConnectionField(ServiceNode)
    
    
    Education = relay.Node.Field(EducationNode)
    all_Education = DjangoFilterConnectionField(EducationNode)
    
    
    DetailCompetence = relay.Node.Field(DetailCompetenceNode)
    all_DetailCompetence = DjangoFilterConnectionField(DetailCompetenceNode)
    
    
    Message = relay.Node.Field(MessageNode)
    all_Message  = DjangoFilterConnectionField(MessageNode)
    
    Users = relay.Node.Field(UserNode)
    all_User  = DjangoFilterConnectionField(UserNode)
    
    Experience = relay.Node.Field(ExperienceNode)
    all_Experience = DjangoFilterConnectionField(ExperienceNode)
    
    
    Competence = relay.Node.Field(CompetenceNode)
    all_competence = DjangoFilterConnectionField(CompetenceNode)