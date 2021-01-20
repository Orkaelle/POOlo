from lettuce import Lettuce
from carrot import Carrot
from bean import Bean

class Gardener:
    def __init__(self, garden):
        self.garden = garden

    def plant(self, vegetable, nb_seed):
        max_seed_to_plant = self.check_capacity(nb_seed)
        if max_seed_to_plant != nb_seed :
            print (f'Garden full !')
        print(f'{max_seed_to_plant} seed(s) of {vegetable.type} planted.')

        vegetable.grow(max_seed_to_plant)
        self.garden.add(vegetable)

        return vegetable
    
    def check_capacity(self, nb_seed):
        remaining_places = 30 - self.garden.seed
        return min(remaining_places, nb_seed)
