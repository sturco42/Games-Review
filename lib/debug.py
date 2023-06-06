#!/usr/bin/env python3
import ipdb

from classes.game import Game
from classes.customer import Customer
from classes.review import Review

#Game
# g1 = Game('Call of Duty: Warzone', 'Activision', 2022, 3.9)

#Customer
c1 = Customer('John', 'Smith', 'Gamer NO.1')
# c2 = Customer(1, 'Smith', 'adjhj') => TypeError: First name cannot be blank or number!
# c3 = Customer('John', 'Smith', 'Gamer NO.1') #=> TypeError: This username has been taken, please choose another one.
# c4 = Customer('John', 'Smith', 's') #=> TypeError: This username has been taken, please choose another one.

#Transaction


#Review
# r1 = Review(2, g1, c1)


if __name__ == '__main__':
    print("HELLO! :) let's debug")
    ipdb.set_trace()