from django.shortcuts import render

from rest_framework import generics
from .models import Area, Sala, Camilla, TipoUsuario, Horario, Funcionario, Turno, Actividad, Accion, Registro
from .serializers import AreaSerializer, SalaSerializer, CamillaSerializer, TipoUsuarioSerializer, HorarioSerializer, \
    FuncionarioSerializer, TurnoSerializer, ActividadSerializer, AccionSerializer, RegistroSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


# CRUD Area ------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def vista_lista_crear_area(request):
    if request.method == 'GET':
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_area(request, id):
    try:
        area = Area.objects.get(pk=id)
    except Area.DoesNotExist:
        return Response({'error': 'El área no existe'}, status=404)

    if request.method == 'GET':
        serializer = AreaSerializer(area)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AreaSerializer(area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        area.delete()
        return Response({'message': 'El área ha sido eliminada'})


# CRUD Sala ------------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def vista_lista_crear_sala(request):
    if request.method == 'GET':
        salas = Sala.objects.all()
        serializer = SalaSerializer(salas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SalaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_sala(request, id):
    try:
        sala = Sala.objects.get(pk=id)
    except Sala.DoesNotExist:
        return Response({'error': 'La sala no existe'}, status=404)

    if request.method == 'GET':
        serializer = SalaSerializer(sala)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SalaSerializer(sala, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sala.delete()
        return Response({'message': 'La sala ha sido eliminada'})


# CRUD Camilla ---------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def vista_lista_crear_camilla(request):
    if request.method == 'GET':
        camillas = Camilla.objects.all()
        serializer = CamillaSerializer(camillas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CamillaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_camilla(request, id):
    try:
        camilla = Camilla.objects.get(pk=id)
    except Camilla.DoesNotExist:
        return Response({'error': 'La camilla no existe'}, status=404)

    if request.method == 'GET':
        serializer = CamillaSerializer(camilla)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CamillaSerializer(camilla, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        camilla.delete()
        return Response({'message': 'La camilla ha sido eliminada'})


# CRUD TipoUsuario -----------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def vista_lista_crear_tipo_usuario(request):
    if request.method == 'GET':
        tipos_usuarios = TipoUsuario.objects.all()
        serializer = TipoUsuarioSerializer(tipos_usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TipoUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_tipo_usuario(request, id):
    try:
        tipo_usuario = TipoUsuario.objects.get(pk=id)
    except TipoUsuario.DoesNotExist:
        return Response({'error': 'El tipo de usuario no existe'}, status=404)

    if request.method == 'GET':
        serializer = TipoUsuarioSerializer(tipo_usuario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TipoUsuarioSerializer(tipo_usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tipo_usuario.delete()
        return Response({'message': 'El tipo de usuario ha sido eliminado'})


# CRUD Horario ---------------------------------------------------------------------------------------------------------


@api_view(['GET', 'POST'])
def vista_lista_crear_horario(request):
    if request.method == 'GET':
        horarios = Horario.objects.all()
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HorarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_horario(request, id):
    try:
        horario = Horario.objects.get(pk=id)
    except Horario.DoesNotExist:
        return Response({'error': 'El horario no existe'}, status=404)

    if request.method == 'GET':
        serializer = HorarioSerializer(horario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HorarioSerializer(horario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        horario.delete()
        return Response({'message': 'El horario ha sido eliminado'})


# CRUD Funcionario -----------------------------------------------------------------------------------------------------


@api_view(['GET', 'POST'])
def vista_lista_crear_funcionario(request):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_funcionario(request, id):
    try:
        funcionario = Funcionario.objects.get(pk=id)
    except Funcionario.DoesNotExist:
        return Response({'error': 'El funcionario no existe'}, status=404)

    if request.method == 'GET':
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FuncionarioSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        funcionario.delete()
        return Response({'message': 'El funcionario ha sido eliminado'})


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        rut = request.data['rut']
        dv = request.data['dv']
        contrasena = request.data['contrasena']
        try:
            user = Funcionario.objects.get(rut=str(rut)+"-"+str(dv), contrasena=contrasena)
        except Funcionario.DoesNotExist:
            return Response({'error': 'El usuario no existe'}, status=404)
        serializer = FuncionarioSerializer(user)
        return Response(serializer.data)


# CRUD Turno -----------------------------------------------------------------------------------------------------------


@api_view(['GET', 'POST'])
def vista_lista_crear_turno(request):
    if request.method == 'GET':
        turnos = Turno.objects.all()
        serializer = TurnoSerializer(turnos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TurnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_turno(request, id):
    try:
        turno = Turno.objects.get(pk=id)
    except Turno.DoesNotExist:
        return Response({'error': 'El turno no existe'}, status=404)

    if request.method == 'GET':
        serializer = TurnoSerializer(turno)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TurnoSerializer(turno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        turno.delete()
        return Response({'message': 'El turno ha sido eliminado'})


# CRUD Actividad -------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def vista_lista_crear_actividad(request):
    if request.method == 'GET':
        actividades = Actividad.objects.all()
        serializer = ActividadSerializer(actividades, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActividadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_actividad(request, id):
    try:
        actividad = Actividad.objects.get(pk=id)
    except Actividad.DoesNotExist:
        return Response({'error': 'La actividad no existe'}, status=404)

    if request.method == 'GET':
        serializer = ActividadSerializer(actividad)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActividadSerializer(actividad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        actividad.delete()
        return Response({'message': 'La actividad ha sido eliminada'})


# CRUD Accion ----------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def vista_lista_crear_accion(request):
    if request.method == 'GET':
        acciones = Accion.objects.all()
        serializer = AccionSerializer(acciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_accion(request, id):
    try:
        accion = Accion.objects.get(pk=id)
    except Accion.DoesNotExist:
        return Response({'error': 'La accion no existe'}, status=404)

    if request.method == 'GET':
        serializer = AccionSerializer(accion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AccionSerializer(accion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        accion.delete()
        return Response({'message': 'La accion ha sido eliminada'})


# CRUD Registro --------------------------------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def vista_lista_crear_registro(request):
    if request.method == 'GET':
        registros = Registro.objects.all()
        serializer = RegistroSerializer(registros, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_detalle_actualizar_eliminar_registro(request, id):
    try:
        registro = Registro.objects.get(pk=id)
    except Registro.DoesNotExist:
        return Response({'error': 'El registro no existe'}, status=404)

    if request.method == 'GET':
        serializer = RegistroSerializer(registro)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegistroSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        registro.delete()
        return Response({'message': 'El registro ha sido eliminado'})
