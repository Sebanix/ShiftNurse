from django.shortcuts import render, redirect

from front.controllers.camilla_controller import CamillaController
from front.controllers.area_controller import AreaController
from front.controllers.sala_controller import SalaController
from front.formularios.loginform import LoginForm


def autenticacion_login(request):
    error = ''
    if request.method == 'POST':
        print("login post")
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            dv = form.cleaned_data['dv']
            password = form.cleaned_data['password']

            if rut == '12345678' and dv == '9' and password == '123456':
                return redirect('/dashboard')
            else:
                error = 'Credenciales inválidas'
                return render(request, 'autenticacion/login.html', {'form': form, 'error': error})
        else:
            error = 'Credenciales inválidas'
            return render(request, 'autenticacion/login.html', {'form': form, 'error': error})
    else:
        form = LoginForm()
        return render(request, 'autenticacion/login.html', {'form': form, 'error': error})


def autenticacion_registro(request):
    area_controller = AreaController()
    areas = area_controller.get_all_areas()

    return render(request, 'autenticacion/registro.html', {'areas': areas})


def autenticacion_horario(request):
    return render(request, 'autenticacion/horario.html')


def autenticacion_usuario(request):
    return render(request, 'autenticacion/usuario.html')


def principal_dashboard(request):
    return render(request, 'principal/dashboard.html')


def principal_analisis(request):
    return render(request, 'principal/analisis.html')


def principal_turno(request):
    return render(request, 'principal/turno.html')


def areas_estacion(request):
    area_controller = AreaController()
    areas = area_controller.get_all_areas()

    return render(request, 'areas/estacion.html', {'areas': areas})


def areas_salas(request):
    salas_controller = SalaController()
    salas = salas_controller.get_all_salas()

    area_controller = AreaController()
    areas = area_controller.get_all_areas()
    return render(request, 'areas/sala.html', {'salas': salas, 'areas': areas})


def areas_camillas(request):
    camillas_controller = CamillaController()
    camillas = camillas_controller.get_all_camillas()

    salas_controller = SalaController()
    salas = salas_controller.get_all_salas()

    area_controller = AreaController()
    areas = area_controller.get_all_areas()
    return render(request, 'areas/camilla.html', {'salas': salas, 'areas': areas, 'camillas': camillas})


def administracion_funcionario(request):
    return render(request, 'administracion/funcionario.html')


def actividades_accion(request):
    return render(request, 'actividades/accion.html')


def actividades_actividad(request):
    return render(request, 'actividades/actividad.html')


def actividades_historial(request):
    return render(request, 'actividades/historial.html')


def actividades_registrar(request):
    return render(request, 'actividades/registrar.html')


def actividades_todo(request):
    return render(request, 'actividades/todo.html')
