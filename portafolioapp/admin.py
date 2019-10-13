from django.contrib import admin
from portafolioapp.models import Usuario, Portafolio

# Register your models here.
Models = [Usuario, Portafolio]

admin.site.register(Models)