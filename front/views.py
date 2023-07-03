from django.shortcuts import render, redirect
import requests

from .model_forms import FuncionarioForm, AreaForm, SalaForm, CamillaForm
from .models import Area, Sala, Camilla

urlbase = 'http://127.0.0.1:8000/api/'


def autenticacion_login(request):
    error = ''
    if request.method == 'POST':
        print("login post")
        form = FuncionarioForm(request.POST)

        rut = form.data['rut']
        dv = form.data['dv']
        password = form.data['password']

        url = urlbase + 'login/'

        response = requests.post(url, data={'rut': rut, 'dv': dv, 'contrasena': password})
        data = response.json()

        if response.status_code == 200:
            print('Login exitoso')
            return redirect('/dashboard')
        else:
            print('Error en la solicitud:', response.status_code)
            error = data['error']
            return render(request, 'autenticacion/login.html', {'form': form, 'error': error})

    else:
        form = FuncionarioForm()
        return render(request, 'autenticacion/login.html', {'form': form, 'error': error})


def autenticacion_registro(request):
    url = urlbase + 'areas/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return render(request, 'autenticacion/registro.html', {'areas': data})
    else:
        print('Error en la solicitud:', response.status_code)

    return render(request, 'autenticacion/registro.html')


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
    data = get_areas()

    form = AreaForm()

    if request.method == 'POST':
        form.data = {
            'area': request.POST.get('area'),
            'leyenda': request.POST.get('leyenda')
        }

    codigo = request.GET.get('codigo')
    delete = request.GET.get('delete')

    if delete:
        url = urlbase + 'areas/' + delete + '/'
        response = requests.delete(url)

        if response.status_code == 200:
            print('Area eliminada')
            return redirect('/estacion/')
        else:
            print('Error en la solicitud:', response.status_code)

    if codigo and request.method == 'GET':
        url = urlbase + 'areas/' + codigo + '/'
        response = requests.get(url)

        if response.status_code == 200:

            area: Area = response.json()

            form.data = area

            print(form.data)
            return render(request, 'areas/estacion.html', {'form': form, 'areas': data})
        else:
            print('Error en la solicitud:', response.status_code)
            return render(request, 'areas/estacion.html', {'areas': data})

    if request.method == 'POST':

        if form.data['area'] == '' or form.data['leyenda'] == '':
            print('datos vacios')
            print(form.data)
            return render(request, 'areas/estacion.html', {'form': form, 'areas': data})

        if codigo:

            url = urlbase + 'areas/' + codigo + '/'
            response = requests.put(url, data=form.data)

            if response.status_code == 200:
                return redirect('/estacion/')

        url = urlbase + 'areas/'
        response = requests.post(url, data=form.data)

        if response.status_code == 201:
            return redirect('/estacion/')
        else:
            print('Error en la solicitud:', response.status_code)
            return render(request, 'areas/estacion.html', {'form': form, 'areas': data})

    return render(request, 'areas/estacion.html', {'areas': data})


def get_areas():
    url = urlbase + 'areas/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error en la solicitud:', response.status_code)

    return []


def areas_salas(request):
    areas = get_areas()
    salas = get_salas(areas)

    form = SalaForm()

    if request.method == 'POST':
        form.data = {
            'sala': request.POST.get('sala'),
            'leyenda': request.POST.get('leyenda'),
            'fk_area': request.POST.get('fk_area')
        }

    codigo = request.GET.get('codigo')
    delete = request.GET.get('delete')

    if delete:
        url = urlbase + 'salas/' + delete + '/'
        response = requests.delete(url)

        if response.status_code == 200:
            print('Sala eliminada')
            return redirect('/sala/')
        else:
            print('Error en la solicitud:', response.status_code)

    if codigo and request.method == 'GET':
        url = urlbase + 'salas/' + codigo + '/'
        response = requests.get(url)

        if response.status_code == 200:

            sala: Sala = response.json()

            form.data = sala

            print(form.data)
            return render(request, 'areas/sala.html', {'form': form, 'areas': areas, 'salas': salas})
        else:
            print('Error en la solicitud:', response.status_code)
            return render(request, 'areas/sala.html', {'areas': areas, 'salas': salas})

    if request.method == 'POST':

        if form.data['sala'] == '' or form.data['leyenda'] == '' or form.data['fk_area'] == '':
            print('datos vacios')
            print(form.data)
            return render(request, 'areas/sala.html', {'form': form, 'areas': areas, 'salas': salas})

        if codigo:

            url = urlbase + 'salas/' + codigo + '/'
            response = requests.put(url, data=form.data)

            if response.status_code == 200:
                return redirect('/sala/')

        url = urlbase + 'salas/'
        response = requests.post(url, data=form.data)

        if response.status_code == 201:
            return redirect('/sala/')
        else:
            print('Error en la solicitud:', response.status_code)
            return render(request, 'areas/sala.html', {'form': form, 'areas': areas, 'salas': salas})

    return render(request, 'areas/sala.html', {'form': form, 'salas': salas, 'areas': areas})


def get_salas(areas):
    url = urlbase + 'salas/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for sala in data:
            for area in areas:
                if sala['fk_area'] == area['codigo']:
                    sala['area'] = area['area']
                    break
        print(data)
        return data
    else:
        print('Error en la solicitud:', response.status_code)

    return []


def areas_camillas(request):
    areas = get_areas()
    salas = get_salas(areas)
    camillas = get_camillas(salas)

    form = CamillaForm()

    if request.method == 'POST':
        form.data = {
            'camilla': request.POST.get('camilla'),
            'leyenda': request.POST.get('leyenda'),
            'fk_sala': request.POST.get('fk_sala')
        }

    codigo = request.GET.get('codigo')
    delete = request.GET.get('delete')

    if delete:
        url = urlbase + 'camillas/' + delete + '/'
        response = requests.delete(url)

        if response.status_code == 200:
            print('Camilla eliminada')
            return redirect('/camilla/')
        else:
            print('Error en la solicitud:', response.status_code)

    if codigo and request.method == 'GET':
        url = urlbase + 'camillas/' + codigo + '/'
        response = requests.get(url)

        if response.status_code == 200:

            camilla: Camilla = response.json()

            form.data = camilla

            print(form.data)
            return render(request, 'areas/camilla.html', {'form': form, 'areas': areas, 'salas': salas, 'camillas': camillas})
        else:
            print('Error en la solicitud:', response.status_code)
            return render(request, 'areas/camilla.html', {'areas': areas, 'salas': salas, 'camillas': camillas})

    if request.method == 'POST':

            if form.data['camilla'] == '' or form.data['leyenda'] == '' or form.data['fk_sala'] == '':
                print('datos vacios')
                print(form.data)
                return render(request, 'areas/camilla.html', {'form': form, 'areas': areas, 'salas': salas, 'camillas': camillas})

            if codigo:

                url = urlbase + 'camillas/' + codigo + '/'
                response = requests.put(url, data=form.data)

                if response.status_code == 200:
                    return redirect('/camilla/')

            url = urlbase + 'camillas/'
            response = requests.post(url, data=form.data)

            if response.status_code == 201:
                return redirect('/camilla/')
            else:
                print('Error en la solicitud:', response.status_code)
                return render(request, 'areas/camilla.html', {'form': form, 'areas': areas, 'salas': salas, 'camillas': camillas})

    return render(request, 'areas/camilla.html', {'form': form, 'areas': areas, 'salas': salas, 'camillas': camillas})

def get_camillas(salas):
    url = urlbase + 'camillas/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for camilla in data:
            for sala in salas:
                if camilla['fk_sala'] == sala['codigo']:
                    camilla['sala'] = sala['sala']
                    camilla['area'] = sala['area']
                    break
        print(data)
        return data
    else:
        print('Error en la solicitud:', response.status_code)

    return []

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
