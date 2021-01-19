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
carrot = Poolo.plant('carrot',12)
lettuce = Poolo.plant('lettuce',7)
bean = Poolo.plant('bean',9)

# Invasion de limaces affamées
slug = Slug(garden)

slug.eat(carrot,5)
slug.eat(lettuce,2)
slug.eat(bean,3)

# Vérifions la composition du jardin
print(f'\nLe jardin contient {garden.seed} graine(s) plantée(s), dont:')
print(f'{carrot.seed} graine(s) de carotte,')
print(f'{lettuce.seed} graine(s) de laitue,')
print(f'{bean.seed} graine(s) de haricot.')
