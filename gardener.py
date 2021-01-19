from lettuce import Lettuce
from carrot import Carrot
from bean import Bean

class Gardener:
    def __init__(self, garden):
        self.garden = garden

    def plant(self, vegetable, nb_seed):
        vegetable = vegetable.lower()
        if vegetable == 'lettuce':
            plantation = Lettuce()
        elif vegetable == 'carrot':
            plantation = Carrot()
        elif vegetable == 'bean':
            plantation = Bean()
    
        plantation.grow(nb_seed)
        self.garden.add(plantation)

        return plantation
    
       

