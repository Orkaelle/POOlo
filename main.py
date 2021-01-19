from lettuce import Lettuce
from carrot import Carrot
from bean import Bean
from garden import Garden
from slug import Slug

# Création du jardin
g = Garden()

# Création des légumes
c = Carrot()
l = Lettuce()
b = Bean()

# Plantation
c.grow(8)
l.grow(6)
b.grow(12)

g.add(c)
g.add(l)
g.add(b)

# Invasion de limaces affamées
slug = Slug(g)

slug.eat(c,5)
slug.eat(l,2)
slug.eat(b,3)

# Voyons cb de graines il reste dans le jardin :
print(f'\nLe jardin contient {g.seed} graine(s) plantée(s), dont:')
print(f'{c.seed} graine(s) de carotte,')
print(f'{l.seed} graine(s) de laitue,')
print(f'{b.seed} graine(s) de haricot.')
