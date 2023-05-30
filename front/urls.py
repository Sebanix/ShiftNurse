from django.contrib import admin
from django.urls import path
from front.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', autenticacion_login, name='login'),
    path('registro/', autenticacion_registro, name='registro'),
    path('horario/', autenticacion_horario, name='horario'),
    path('usuario/', autenticacion_usuario, name='usuario'),
    path('dashboard/', principal_dashboard, name='dashboard'),
    path('analisis/', principal_analisis, name='analisis'),
    path('turno/', principal_turno, name='turno'),
    path('estacion/', areas_estacion, name='estacion'),
    path('sala/', areas_salas, name='sala'),
    path('camilla/', areas_camillas, name='camilla'),
    path('funcionario/', administracion_funcionario, name='funcionario'),
    path('accion/', actividades_accion, name='accion'),
    path('actividad/', actividades_actividad, name='actividad'),
    path('historial/', actividades_historial, name='historial'),
    path('registrar/', actividades_registrar, name='registrar'),
    path('todo/', actividades_todo, name='todo'),
]
