from django.test import TestCase, Client
from rest_framework.utils import json
from portafolioapp.models import Usuario, Portafolio
from django.contrib.auth.models import User
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

    def test_listado_portafolio_publico(self):
        user_model = Usuario.objects.create(nombres='Elkin', apellidos='Mantill', username='emantilla',
                                            url_foto='https://vignette.wikia.nocookie.net/leagueoflegends/images/a/a6/Jax_OriginalCentered.jpg/revision/latest/scale-to-width-down/1215?cb=20180414203245',
                                            perfil_prof='Ing Sistemas')
        Portafolio.objects.create(titulo='jax', url_imag='', descripcion='pepito peres', tipo_archivo='jpg',
                                  is_private=True, owner=user_model)
        Portafolio.objects.create(titulo='jarvan', url_imag='', descripcion='ojo', tipo_archivo='jpg',
                                  is_private=False, owner=user_model)
        Portafolio.objects.create(titulo='ana', url_imag='', descripcion='viento', tipo_archivo='jpg',
                                  is_private=False, owner=user_model)

        url = '/portafolio/publicos/'
        response = self.client.get(url, {'username': 'emantilla', 'is_private': False})
        print(response.content)
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 2)

    def test_login(self):
        User.objects.create_user(username='emantilla', password='abcd123')
        url = '/portafolio/login/'

        response = self.client.get(url, {'username': 'emantilla', 'password': 'abcd123'})
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'], 'emantilla')

    def test_modifica_datos(self):
        user_model = Usuario.objects.create(nombres='Elkin', apellidos='Mantill', username='emantilla',
                                            url_foto='https://vignette.wikia.nocookie.net/leagueoflegends/images/a/a6/Jax_OriginalCentered.jpg/revision/latest/scale-to-width-down/1215?cb=20180414203245',
                                            perfil_prof='Ing Sistemas')
        url = '/portafolio/editar/'
        response = self.client.put(url, json.dumps({"nombres": "Juan Camilo", "apellidos": "Cardenas", "username": "emantilla",
                                            "url_foto": "https://www.google.com",
                                            "perfil_prof": "Ing Sistemas"}), content_type='aplication/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['nombres'], 'Juan Camilo')

