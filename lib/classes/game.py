import sqlite3
CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor()

class Game:

    def __init__(self, title, publisher, year):
        self.title = title
        self.publisher = publisher
        self.year = year
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str) or 1 >= len(title) >= 30:
            raise TypeError('The title must be a string between 1 and 30 characters!')
        self._title = title
        
    @property
    def publisher(self):
        return self._publisher
    
    @publisher.setter
    def publisher(self, publisher):
        if not isinstance(publisher, str) or 1 >= len(publisher) >= 30:
            raise TypeError('The publisher must be a string between 1 and 30 characters!')
        self._publisher = publisher
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if not isinstance(year, int) or 1900 >= year >= 2300:
            raise TypeError('The year must be an integer between 1900 and 2300')
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
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]
        
    @classmethod
    def find_by_title(cls, title):
        CURSOR.execute("""
            SELECT * FROM games
            WHERE title is ?;
        """, (title, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None       


from classes.customer import Customer
from classes.review import Review
from statistics import mean
