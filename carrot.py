from vegetable import Vegetable

class Carrot(Vegetable) :
    def __init__(self):
        self.seed = 0

    def grow(self, number=0):
        self.seed += number
