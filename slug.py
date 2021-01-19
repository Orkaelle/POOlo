from lettuce import Lettuce
from carrot import Carrot
from bean import Bean

class Slug:
    def __init__(self, garden):
        self.garden = garden

    def eat(self, food, ration):     
        food.grow(-ration)
        self.garden.seed -= ration

