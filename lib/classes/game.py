from classes.__init__ import CONN, CURSOR

class Game:
    
    def __init__(self, title, publisher, year, id=None):
        self.title = title
        self.publisher = publisher
        self.year = year
        self.id = id
    
    def __repr__(self):
        return f"<Game {self.id}. {self.title} | Publisher: {self.publisher} | Year: {self.year}>"

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
            WHERE lower(title) is ?;
        """, (title.lower(), ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0]) if row else None

    @classmethod
    def find_by_year(cls, year):
        CURSOR.execute("""
            SELECT * FROM games
            WHERE year is ?;
        """, (year, ))
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def ave_rating(cls, id):
        CURSOR.execute("""
            SELECT * FROM reviews
            WHERE game_id is ?;
        """, (id, ))
        rows = CURSOR.fetchall()
        if rows:
            return mean([list(row)[1] for row in rows])
        else:
            print('There is no rating for this game yet')

    @classmethod
    def average_rating_no_print(cls, id):
        CURSOR.execute("""
            SELECT * FROM reviews
            WHERE game_id is ?;
        """, (id, ))
        rows = CURSOR.fetchall()
        if rows:
            return mean([list(row)[1] for row in rows])
            
    @classmethod
    def highest_rated_games(cls):
        CURSOR.execute("""
            SELECT id FROM games
        """)
        rows = CURSOR.fetchall()
        def mySortFunc(gameRating):
            return gameRating[1]
        if rows:
            game_ratings = []
            for row in rows:
                id = row[0]
                average_rating = Game.average_rating_no_print(id)
                if average_rating != None:
                    game_ratings.append((id, average_rating))
            
            game_ratings.sort(reverse=True, key=mySortFunc)
            top_10_games = game_ratings[0:10]
            for id, rating in top_10_games:
                game_details_by_id(id)

from classes.user import User
from classes.review import Review
from statistics import mean
from helpers import (game_details_by_id)