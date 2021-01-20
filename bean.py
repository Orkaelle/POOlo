from vegetable import Vegetable

class Bean(Vegetable) :
    def __init__(self):
        self.seed = 0
        self.type = 'bean'

    def grow(self, number=0):
        self.seed += number
