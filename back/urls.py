from django.urls import path
from . import views

urlpatterns = [
    # URLs para el modelo Area
    path('areas/', views.vista_lista_crear_area),
    path('areas/<int:id>/', views.vista_detalle_actualizar_eliminar_area),

    # URLs para el modelo Sala
    path('salas/', views.vista_lista_crear_sala),
    path('salas/<int:id>/', views.vista_detalle_actualizar_eliminar_sala),

    # URLs para el modelo Camilla
    path('camillas/', views.vista_lista_crear_camilla),
    path('camillas/<int:id>/', views.vista_detalle_actualizar_eliminar_camilla),

    # URLs para el modelo TipoUsuario
    path('tipos_usuarios/', views.vista_lista_crear_tipo_usuario),
    path('tipos_usuarios/<int:id>/', views.vista_detalle_actualizar_eliminar_tipo_usuario),

    # URLs para el modelo Horario
    path('horarios/', views.vista_lista_crear_horario),
    path('horarios/<int:id>/', views.vista_detalle_actualizar_eliminar_horario),

    # URLs para el modelo Funcionario
    path('funcionarios/', views.vista_lista_crear_funcionario),
    path('funcionarios/<int:id>/', views.vista_detalle_actualizar_eliminar_funcionario),

    path('login/', views.login),

    # URLs para el modelo Turno
    path('turnos/', views.vista_lista_crear_turno),
    path('turnos/<int:id>/', views.vista_detalle_actualizar_eliminar_turno),

    # URLs para el modelo Actividad
    path('actividades/', views.vista_lista_crear_actividad),
    path('actividades/<int:id>/', views.vista_detalle_actualizar_eliminar_actividad),

    # URLs para el modelo Accion
    path('acciones/', views.vista_lista_crear_accion),
    path('acciones/<int:id>/', views.vista_detalle_actualizar_eliminar_accion),

    # URLs para el modelo Registro
    path('registros/', views.vista_lista_crear_registro),
    path('registros/<int:id>/', views.vista_detalle_actualizar_eliminar_registro),
]