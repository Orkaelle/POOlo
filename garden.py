from lettuce import Lettuce
from carrot import Carrot
from bean import Bean


class Garden:
    def __init__(self):
        self.vegetables = []
        self.seed = 0
    
    def add(self, cls):
        self._plant(cls)

    def _plant(self, cls):
        self.vegetables.append(cls)
        self.seed += cls.seed


