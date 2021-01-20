from src.lettuce import Lettuce
from src.carrot import Carrot
from src.bean import Bean
from src.garden import Garden
from src.slug import Slug
from src.gardener import Gardener

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
print(f'\nThe garden contain {garden.seed} seed(s), for {Garden.nb_type} vegetable type(s) :')
print(f'{carrot.seed} seed(s) of carrot,')
print(f'{lettuce.seed} seed(s) of lettuce,')
print(f'{bean.seed} seed(s) of bean.')
