from django.urls import path
from portafolioapp import views

urlpatterns = [
    path('', views.index_portafolios, name="index"),
    path('registrar/', views.create_user, name="create_user")
]
