from front.model.sala_model import Sala


class Camilla:

    def __init__(self, id: int, num: int, sala: Sala):
        self.id = id
        self.num = num
        self.sala = sala

    def __str__(self):
        return f'{self.sala}' + "{:03d}".format(self.num)

