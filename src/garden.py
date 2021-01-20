from src.lettuce import Lettuce
from src.carrot import Carrot
from src.bean import Bean


class Garden:
    nb_type = 0

    def __init__(self):
        self.vegetables = []
        self.seed = 0
    
    def add(self, cls):
        self._plant(cls)

    def _plant(self, cls):
        if not cls in self.vegetables :
            self.vegetables.append(cls)
        self.seed = self.get_total_seed()
        list_type = [ type(v) for v in self.vegetables ]
        Garden.nb_type = len(set(list_type))

    def get_total_seed(self):
        total_seed = 0
        for v in self.vegetables :
            total_seed += v.seed
        return total_seed







