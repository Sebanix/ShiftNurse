from django.urls import path
from . import views

urlpatterns = [
    path('areas/', views.vista_lista_crear_area),
    path('areas/<int:id>/', views.vista_detalle_actualizar_eliminar_area),

    path('salas/', views.vista_lista_crear_sala),
    path('salas/<int:id>/', views.vista_detalle_actualizar_eliminar_sala),

    path('camillas/', views.vista_lista_crear_camilla),
    path('camillas/<int:id>/', views.vista_detalle_actualizar_eliminar_camilla),

    path('tipos_usuarios/', views.vista_lista_crear_tipo_usuario),
    path('tipos_usuarios/<int:id>/', views.vista_detalle_actualizar_eliminar_tipo_usuario),

    path('horarios/', views.vista_lista_crear_horario),
    path('horarios/<int:id>/', views.vista_detalle_actualizar_eliminar_horario),

    path('funcionarios/', views.vista_lista_crear_funcionario),
    path('funcionarios/<int:id>/', views.vista_detalle_actualizar_eliminar_funcionario),

    path('login/', views.login),

    path('turnos/', views.vista_lista_crear_turno),
    path('turnos/<int:id>/', views.vista_detalle_actualizar_eliminar_turno),

    path('actividades/', views.vista_lista_crear_actividad),
    path('actividades/<int:id>/', views.vista_detalle_actualizar_eliminar_actividad),

    path('acciones/', views.vista_lista_crear_accion),
    path('acciones/<int:id>/', views.vista_detalle_actualizar_eliminar_accion),

    path('registros/', views.vista_lista_crear_registro),
    path('registros/<int:id>/', views.vista_detalle_actualizar_eliminar_registro),
]