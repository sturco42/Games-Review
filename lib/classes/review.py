class Review:
    
    all = []
    
    def __init__(self, stars, game, customer):
        self.stars = stars
        self.game = game
        self.customer = customer
        type(self).all.append(self)

    @property
    def stars(self):
        return self._stars
    
    @stars.setter
    def stars(self, stars):
        if isinstance(stars, int) and 1 <= len(stars) <= 5:
            self._stars = stars
            
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise TypeError('game must be of the type Game')
        self._game = game
    
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError('customer must be of the type Customer')
        self._customer = customer

from customer import Customer
from game import Game