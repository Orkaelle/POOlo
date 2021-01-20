from src.vegetable import Vegetable

class Lettuce(Vegetable) :
    def __init__(self):
        self.seed = 0
        self.type = 'lettuce'

    def grow(self, number=0):
        self.seed += number
        


