from django import forms
from .models import Area, Sala, Camilla, TipoUsuario, Horario, Funcionario, Turno, Actividad, Accion, Registro


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'


class CamillaForm(forms.ModelForm):
    class Meta:
        model = Camilla
        fields = '__all__'


class TipoUsuarioForm(forms.ModelForm):
    class Meta:
        model = TipoUsuario
        fields = '__all__'


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'


class AccionForm(forms.ModelForm):
    class Meta:
        model = Accion
        fields = '__all__'


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'