from lettuce import Lettuce
from carrot import Carrot
from bean import Bean
from garden import Garden

g = Garden()
g.add(Carrot())

b = Bean()
b.grow(8)
g.add(b)

print(g.seed) # display 8