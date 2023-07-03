from django.db import models

from django.db import models

from django.db import models


class Area(models.Model):
    codigo = models.AutoField(primary_key=True)
    area = models.CharField(max_length=50)
    leyenda = models.CharField(max_length=50)


class Sala(models.Model):
    codigo = models.AutoField(primary_key=True)
    sala = models.CharField(max_length=50)
    leyenda = models.CharField(max_length=50)
    fk_area = models.ForeignKey(Area, on_delete=models.CASCADE)


class Camilla(models.Model):
    codigo = models.AutoField(primary_key=True)
    camilla = models.CharField(max_length=50)
    leyenda = models.CharField(max_length=50)
    fk_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)


class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)


class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    entrada = models.TimeField()
    salida = models.TimeField()


class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    contrasena = models.IntegerField()
    fk_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    fk_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    fk_horario = models.ForeignKey(Horario, on_delete=models.CASCADE)


class Turno(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=50)
    fk_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)


class Actividad(models.Model):
    id = models.AutoField(primary_key=True)
    actividad = models.CharField(max_length=50)


class Accion(models.Model):
    id = models.AutoField(primary_key=True)
    accion = models.CharField(max_length=50)


class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.CharField(max_length=50)
    completado = models.BooleanField()
    fk_actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fk_accion = models.ForeignKey(Accion, on_delete=models.CASCADE)
    fk_area = models.ForeignKey(Area, on_delete=models.CASCADE)
    fk_sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fk_camilla = models.ForeignKey(Camilla, on_delete=models.CASCADE)

