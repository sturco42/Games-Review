class Review:
    
    all = []
    
    def __init__(self, rating, game, customer):
        self.rating = rating
        self.game = game
        self.customer = customer
        type(self).all.append(self)

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 10:
            self._rating = rating
        else:
            raise AttributeError('The rating must be an integer between 1 and 10')
            
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise TypeError('The game must be of the type Game.')
        self._game = game
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError('customer must be of the type Customer')
        self._customer = customer

from .customer import Customer
from .game import Game
