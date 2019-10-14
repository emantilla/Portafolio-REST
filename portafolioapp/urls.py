from django.urls import path
from portafolioapp import views

urlpatterns = [
    path('', views.index_portafolios, name="index"),
    path('registrar/', views.create_user, name="create_user"),    
    path('publicos/', views.portafolios_pub, name='publicos'),
    path('login/', views.login_user, name='login'),
    path('editar/', views.update_profile, name='login')
]
