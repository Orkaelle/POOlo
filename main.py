from lettuce import Lettuce
from carrot import Carrot
from bean import Bean
from garden import Garden
from slug import Slug
from gardener import Gardener

# Création du jardin et du jardinier
garden = Garden()
Poolo = Gardener(garden)

# Création des légumes
carrot = Carrot()
lettuce = Lettuce()
bean = Bean()

# Plantation
carrot = Poolo.plant(carrot,12)
lettuce = Poolo.plant(lettuce,7)
bean = Poolo.plant(bean,9)

# Invasion de limaces affamées
slug = Slug(garden)

slug.eat(carrot,5)
slug.eat(lettuce,2)
slug.eat(bean,3)


# Plantation
carrot = Poolo.plant(carrot,6)
lettuce = Poolo.plant(lettuce,5)
bean = Poolo.plant(bean,13)


# Vérifions la composition du jardin
total_seed, nb_lettuce, nb_carrot, nb_bean = Poolo.count_seed()
print(f'\nLe jardin contient {garden.seed} graine(s) plantée(s), pour {Garden.nb_type} types de légumes :')
print(f'{nb_carrot} graine(s) de carotte,')
print(f'{nb_lettuce} graine(s) de laitue,')
print(f'{nb_bean} graine(s) de haricot.')
