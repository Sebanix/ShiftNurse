class Area:
    def __init__(self, id, name, surfix):
        self.id = id
        self.name = name
        self.surfix = surfix

    def __str__(self):
        return f'{self.id} - {self.name} - {self.surfix}'
