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
        if isinstance(stars, int) and 1 <= stars <= 5:
            self._stars = stars
        else:
            raise AttributeError('The rating must be an integer between 1 and 5')
            
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
            raise TypeError('The customer must be of the type Customer')
        self._customer = customer
        
from classes.customer import Customer
from classes.game import Game