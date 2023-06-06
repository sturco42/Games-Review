class Transaction:
    all = []

    def __init__(self, game, customer):
        self.game = game
        self.customer = customer
        type(self).all.append(self)
