from django.test import TestCase, Client
from rest_framework.utils import json
from portafolioapp.models import Usuario, Portafolio
import json

# Create your tests here.

class PortafolioTestCase(TestCase):
    def test_list_portafolios(self):
        url = '/portafolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_count_portafolios(self):
        user_model = Usuario.objects.create(nombres = 'Elkin', apellidos='Mantill', username='emantilla', url_foto='https://vignette.wikia.nocookie.net/leagueoflegends/images/a/a6/Jax_OriginalCentered.jpg/revision/latest/scale-to-width-down/1215?cb=20180414203245', perfil_prof ='Ing Sistemas')
        Portafolio.objects.create(titulo='jax', url_imag='', descripcion='pepito peres',tipo_archivo='jpg', is_private=True, owner=user_model)
        Portafolio.objects.create(titulo='jarvan', url_imag='', descripcion='ojo', tipo_archivo='jpg',
                                  is_private=False, owner=user_model)
        Portafolio.objects.create(titulo='ana', url_imag='', descripcion='viento', tipo_archivo='jpg',
                                  is_private=False, owner=user_model)
        response = self.client.get('/portafolio/')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data),3)

    def test_registrar_usuario(self):
        url = '/portafolio/registrar/'
        response =self.client.post(url, json.dumps({"nombres":"Juan Camilo", "apellidos":"Cardenas", "username":"jcardenas",
                                            "url_foto":"https://www.google.com",
                                            "perfil_prof":"Ing Sistemas"}),content_type='aplication/json')
        current_data=json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['nombres'],'Juan Camilo')
