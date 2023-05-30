from front.model.area_model import Area


class Sala:
    def __init__(self, id: int, num: int, area: Area):
        self.id = id
        self.num = num
        self.area = area

    def __str__(self):
        return f'{self.area.surfix}' + "{:03d}".format(self.num)
