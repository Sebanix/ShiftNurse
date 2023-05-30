from front.controllers.sala_controller import SalaController
from front.model.camilla_model import Camilla


class CamillaController:
    camillas = []

    def __init__(self):
        self.camillas = []
        contador_id = 1
        for sala in SalaController().get_all_salas():
            for i in range(1, 4):
                self.camillas.append(Camilla(contador_id, i, sala))
                contador_id += 1

    def get_all_camillas(self):
        return self.camillas

    def get_camilla_by_id(self, camilla_id: int):
        for camilla in self.camillas:
            if camilla.id == camilla_id:
                return camilla
        return None

    def get_camilla_by_num(self, camilla_num: int):
        for camilla in self.camillas:
            if camilla.num == camilla_num:
                return camilla
        return None

    def get_camilla_by_sala(self, sala_id: int):
        camillas_filter = []
        for camilla in self.camillas:
            if camilla.sala.id == sala_id:
                camillas_filter.append(camilla)
        return camillas_filter

    def create_camilla(self, camilla: Camilla):
        self.camillas.append(camilla)
        return camilla

    def update_camilla(self, camilla: Camilla):
        for c in self.camillas:
            if c.id == camilla.id:
                c.num = camilla.num
                c.sala = camilla.sala
                return c
        return None

    def delete_camilla(self, camilla_id: int):
        for camilla in self.camillas:
            if camilla.id == camilla_id:
                self.camillas.remove(camilla)
                return camilla
            return None
