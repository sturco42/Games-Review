
from classes.review import Review
from classes.game import Game
from classes.customer import Customer

import ipdb

import sqlite3
CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor()

# customer = Customer('Matteo', 'Pat', )
# game1 = Game('title', 'publi', 2000)

# review1 = Review(3, game1, customer)
# review2 = Review(5, game1, customer)
# print(game1.average_score())

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
Customer.create_table()
Customer.drop_table()

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    ipdb.set_trace()
