from django.shortcuts import render
from portafolioapp.models import Usuario, Portafolio
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json

# Create your views here.
