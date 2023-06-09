from classes.__init__ import CONN, CURSOR

class Review:
    
    def __init__(self, rating, game_id, user_id, id=None):
        self.rating = rating
        self.game_id = game_id
        self.user_id = user_id
        self.id = id

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
        return Game.find_by_game_id(self.game_id)
    
    @game.setter
    def game(self, game_id):
        if not isinstance(game_id, int) or not Game.find_by_game_id(game_id):
            raise Exception('The game must have the correctly associeted attribute!.')
        self._game_id = game_id
    
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user):
        if not isinstance(user, User):
            raise Exception('The user must have the correctly associated attribute!')
        self._user = user

    def save(self):
        CURSOR.execute("""
            INSERT INTO reviews (rating, game_id, user_id)
            VALUES ( ?, ?, ?)
        """, (self.rating, self.game_id, self.user_id))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create_review(cls, rating, game_id, user_id):
        new_review = cls( rating, game_id, user_id)
        new_review.save()
        return new_review

from classes.user import User
from classes.game import Game