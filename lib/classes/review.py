class Review:
    
    def __init__(self, rating, game, user):
        self.rating = rating
        self.game = game
        self.user = user

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1 <= rating <= 10:
            self._rating = rating
        else:
            raise Exception('The rating must be an integer between 1 and 10')
            
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise Exception('The game must have the correctly associeted attribute!.')
        self._game = game
    
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user):
        if not isinstance(user, User):
            raise Exception('The user must have the correctly associated attribute!')
        self._user = user

from classes.user import User
from classes.game import Game
