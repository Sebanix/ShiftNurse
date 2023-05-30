from front.model.area_model import Area


class AreaController:
    areas = []

    def __init__(self):
        self.areas = [Area(1, 'Pediatria', 'PD'),
                      Area(2, 'Traumatologia', 'TM'),
                      Area(3, 'Cardiologia', 'CD'),
                      Area(4, 'Neurologia', 'NL'),
                      Area(5, 'Oftalmologia', 'OF'),
                      Area(6, 'Odontologia', 'OD'),
                      Area(7, 'Ginecologia', 'GN'),
                      Area(8, 'Urologia', 'UR'),
                      Area(9, 'Dermatologia', 'DM'),
                      Area(10, 'Psiquiatria', 'PS')]

    def get_all_areas(self):
        return self.areas

    def get_area_by_id(self, area_id: int):
        for area in self.areas:
            if area.id == area_id:
                return area
        return None

    def get_area_by_name(self, area_name: str):
        for area in self.areas:
            if area.name == area_name:
                return area
        return None

    def get_area_by_surfix(self, area_surfix: str):
        for area in self.areas:
            if area.surfix == area_surfix:
                return area
        return None

    def create_area(self, area: Area):
        self.areas.append(area)
        return area

    def update_area(self, area: Area):
        for a in self.areas:
            if a.id == area.id:
                a.name = area.name
                return a
        return None

    def delete_area(self, area_id: int):
        for area in self.areas:
            if area.id == area_id:
                self.areas.remove(area)
                return area
        return None
