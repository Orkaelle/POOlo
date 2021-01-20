import abc

class Vegetable (abc.ABC):
    def __init__(self):
        self.seed = 0

    @abc.abstractmethod
    def grow(self, number=0):
        pass



