from src.lettuce import Lettuce
from src.carrot import Carrot
from src.bean import Bean
from src.garden import Garden

g = Garden()
g.add(Carrot())

b = Bean()
b.grow(8)
g.add(b)

print(g.seed) # display 8