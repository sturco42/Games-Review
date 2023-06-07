#!/usr/bin/env python3

from classes.review import Review
from classes.game import Game
from classes.user import User

import ipdb

# customer = Customer('Matteo', 'Pat', )
# game1 = Game('title', 'publi', 2000)

# review1 = Review(3, game1, customer)
# review2 = Review(5, game1, customer)
# print(game1.average_score())



#Game

#Customer
c1 = User.create_user('John', 'Smith')
# c2 = User(1, 'Smith') => TypeError: First name cannot be blank or number!
# c3 = User('John', 'Smith') #=> TypeError: This username has been taken, please choose another one.
# c4 = User('John', 'Smith') #=> TypeError: This username has been taken, please choose another one.

#Transaction


#Review
r1 = Review(2, 2, c1.id)
r1.save()
if __name__ == '__main__':
    print("HELLO! :) let's debug")
    ipdb.set_trace()
