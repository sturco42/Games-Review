from classes.__init__ import CONN, CURSOR
class Game:
    
    def __init__(self, title, publisher, year, id=None):
        self.title = title
        self.publisher = publisher
        self.year = year
        self.id = id
    
    def __repr__(self):
        return f"<Game {self.id}. {self.title} | Publisher: {self.publisher} | Year: {self.year}>"

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str) or 1 >= len(title) >= 30:
            raise Exception('The title must be a string between 1 and 30 characters!')
        self._title = title
        
    @property
    def publisher(self):
        return self._publisher
    
    @publisher.setter
    def publisher(self, publisher):
        if not isinstance(publisher, str) or 1 >= len(publisher) >= 30:
            raise Exception('The publisher must be a string between 1 and 30 characters!')
        self._publisher = publisher
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if not isinstance(year, int) or 1900 >= year >= 2300:
            raise Exception('The year must be an integer between 1900 and 2300')
        self._year = year
    
    def average_score(self):
            scores = [review.stars for review in Review.all if review.game is self]
            return mean(scores) if len(scores) else 'N/A'
    
    @classmethod
    def all(cls):
        CURSOR.execute("""
            SELECT * FROM games;
        """)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]
        
    @classmethod
    def find_by_game_id(cls, game_id):
        CURSOR.execute("""
            SELECT * FROM games
            WHERE id is ?;
        """, (game_id, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0]) if row else None       

    @classmethod
    def find_by_title(cls, title):
        CURSOR.execute("""
            SELECT * FROM games
            WHERE title is ?;
        """, (title, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None       

    @classmethod
    def find_by_year(cls, year):
        CURSOR.execute("""
            SELECT * FROM games
            WHERE year is ?;
        """, (year, ))
        rows = CURSOR.fetchone()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]      


from classes.user import User
from classes.review import Review
from statistics import mean
