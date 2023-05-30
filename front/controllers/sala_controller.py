from front.controllers.area_controller import AreaController
from front.model.sala_model import Sala


class SalaController:
    salas = []

    def __init__(self):
        self.salas = []
        contador_id = 1
        for area in AreaController().get_all_areas():
            for i in range(1, 4):
                self.salas.append(Sala(contador_id, i, area))
                contador_id += 1

    def get_all_salas(self):
        return self.salas

    def get_sala_by_id(self, sala_id: int):
        for sala in self.salas:
            if sala.id == sala_id:
                return sala
        return None

    def get_sala_by_num(self, sala_num: int):
        for sala in self.salas:
            if sala.num == sala_num:
                return sala
        return None

    def get_sala_by_area(self, area_id: int):
        salas_filter = []
        for sala in self.salas:
            if sala.area.id == area_id:
                salas_filter.append(sala)
        return salas_filter

    def create_sala(self, sala: Sala):
        self.salas.append(sala)
        return sala

    def update_sala(self, sala: Sala):
        for s in self.salas:
            if s.id == sala.id:
                s.num = sala.num
                s.area = sala.area
                return s
        return None

    def delete_sala(self, sala_id: int):
        for sala in self.salas:
            if sala.id == sala_id:
                self.salas.remove(sala)
                return sala
        return None
