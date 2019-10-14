from django.shortcuts import render
from portafolioapp.models import Usuario, Portafolio
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

@csrf_exempt
def index_portafolios(request):
    portafolios_list = Portafolio.objects.all()    
    return HttpResponse(serializers.serialize('json', portafolios_list))

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        nombres = json_user['nombres']
        apellidos = json_user['apellidos']
        username = json_user['username']
        url_foto = json_user['url_foto']
        perfil_prof = json_user['perfil_prof']

        user_model = Usuario.objects.create(nombres=nombres, apellidos=apellidos, username=username, url_foto=url_foto, perfil_prof=perfil_prof)
        user_model.save()
    
    return HttpResponse(serializers.serialize('json', [user_model]))

@csrf_exempt
def portafolios_pub(request): 
    username = request.GET['username']
    private = request.GET['is_private']
    user = Usuario.objects.filter(username=username)
    portf_pub = Portafolio.objects.filter(owner=user[0]).filter(is_private=private)    

    return HttpResponse(serializers.serialize('json', portf_pub))

@csrf_exempt
def login_user(request):
    username = request.GET['username']
    passwd = request.GET['password']
    user = authenticate(username=username, password=passwd)
    if user:
        login(request, user)    
        return HttpResponse(serializers.serialize("json", [user]))
    else:
        resp = []
        return HttpResponse(serializers.serialize(resp))

