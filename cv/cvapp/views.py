from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
import requests
import json
from . import models
from django.contrib.auth.models import User
from django.core.validators import validate_email

# Fonction d'envoie de  mail
def sendnanmail(fromemail, to, subject, message):
    url = 'https://nan.nan.ci/nanmail'
    try:
        messagehtml =  message 
        donner = {
            'subject':subject,
            'message':messagehtml,
            'to':to,
            'key':'&E)H@McQfTjWnZr4u7w!z%C*F-JaNdRg'
        }
        req = requests.post(url, data = donner)
        if req.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        text =  str(e)
        print ('Message erreur mail --------- ', str(e))
        return False




# Create your views here.
def islogin(request):
    try:
        
        UserModel = get_user_model()
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = ''
        # print(email,password)
        
        isSuccess=False
        try:
            u = UserModel.objects.get(email=email)
            username = u.username

            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_active:
                # print("user is login")
                print(request.user.username)
                isSuccess = True
                login(request, user)

                datas = {
                    'success':True,
                    'username':username,
                    'message':'Votre connection a reussi avec succes',
                }
                return JsonResponse(datas,safe=False) # page si connect
                    
            else:
                data = {
                'success':False,
                'message':'Vos identifiants ne sont pas correcte',
                }
                return JsonResponse(data,safe=False)
            return JsonResponse(datas, safe=False)
        except:
            data = {
                'success':False,
                'message':'Vos identifiants ne sont pas correcte',
            }
            return JsonResponse(data,safe=False)
    except Exception as e:
        print('zzzzzzzz',str(e))
        return redirect('graph')
    
    
# Api de creation de Utilisateur de DJango via  
    
def registerUser(request):

    try:
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        adresse = request.POST.get('adresse')
        specialite = request.POST.get('specialite')
        numero = request.POST.get('numero')
        git = request.POST.get('git')
        facebook = request.POST.get('facebook')
        link = request.POST.get('link')
        
        issucces = False
        text = ''
        is_email = False

        try:
                validate_email(email)
                is_email = True
        except:
            datas = {
                'success': False,
                'message': 'Veuillez entrez un email correcte',
            }
        try:
        
            if numero !='' and not numero.isspace() and nom != '' and not nom.isspace() and prenom != '' and not prenom.isspace()  and email != '' and not email.isspace() and password != '' and not password.isspace() and username != '' and not username.isspace():
                if is_email:
                    # Creation de l'User 
                    user = User(username = username, first_name = nom, last_name = prenom, email = email)
                    user.save()
                    
                    # Enregistrement des Information de du Profile de L'user Exend de Django 
    
                    user.user_profile.specialite = specialite
                    user.user_profile.adresse = adresse
                    user.user_profile.photo = image
                    user.user_profile.facebook = facebook
                    user.user_profile.numero = numero
                    user.user_profile.github = git
                    user.user_profile.lindkedin = link
                    user.user_profile.email = email
                    
                    # Enregistrement du mots de Pass du Nouveau Utilisateur creer desactivation du compte
    
                    user.password = password
                    user.set_password(user.password)
                    user.is_active = False
                    user.save()
                    
                    
                    # envoie  Message de Confirmation du mots pass 
                    current_site = get_current_site(request)
                    mail_subject = 'Activate your blog account.'
                    messages = render_to_string('acc_active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                        'token':account_activation_token.make_token(user),
                    })
                    
                    
                    sendnanmail('guindo@nan.ci',email,'Confirmation de mail ',messages)
                  
                    issucces = True
                    text =  " Verifier Votre adresse mail Pour confirmer votre inscription"
                    
                
                  
                    
                else:
                    issucces = False
                    text = 'Saisir Une Adresse E-mail Valide'
            else:
                issucces = False
                text = 'Veuillez remplir correctement les champs' 
        except Exception as e:
            issucces = False
            text =  str(e)
            print ('Message erreur --------- ', str(e))
        
        datas = {
            'succes': issucces,
            'text': text
        }
        return JsonResponse(datas, safe=False)
    except Exception as e:
        print('',str(e))
        return redirect('graph')
    
    

# Fonction d'activation du compte
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, models.MyUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        return redirect('graph')
    else:
        return render(request, 'account/invalid_link.html')