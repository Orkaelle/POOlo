from lettuce import Lettuce
from carrot import Carrot
from bean import Bean

class Slug:
    def __init__(self, garden):
        self.garden = garden

    def eat(self, food, ration):
        max_seed_to_eat = self.check_stock(food, ration)

        food.grow(-max_seed_to_eat)
        self.garden.add(food)

        print(f'WARNING !! Slugs invasion !! {max_seed_to_eat} seed(s) of {food.type} destroyed !')

    def check_stock(self, food, ration):
        remaining_seed = 0
        for v in self.garden.vegetables :
            if v.type == food.type:
                remaining_seed += v.seed
        return min(remaining_seed, ration)

