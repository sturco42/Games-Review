from classes.review import Review
from classes.game import Game
from classes.customer import Customer

import ipdb

customer = Customer('Matteo', 'Pat')
game1 = Game('title', 'publi', 2000)

review1 = Review(3, game1, customer)
review2 = Review(5, game1, customer)
print(game1.average_score())