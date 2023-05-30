from front.model.accion_model import Accion


class Actividad:
    def __init__(self, id: int, name: str, accion: Accion):
        self.id = id
        self.name = name
        self.accion = accion

    def __str__(self):
        return f'{self.accion.name}' + " : " + f'{self.name}'
