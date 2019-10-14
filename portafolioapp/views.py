from django.shortcuts import render
from portafolioapp.models import Usuario, Portafolio
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

@csrf_exempt
def index_portafolios(request):
    portafolios_list = {"response": "success"}
    # return HttpResponse(serializers.serialize("json", portafolios_list))
    return JsonResponse(portafolios_list, )