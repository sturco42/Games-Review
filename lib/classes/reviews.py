class Review:
    
    all = []
    
    def __init__(self, stars, game, customer):
        self.stars = stars
        self.game = game
        self.customer = customer
        type(self).all.append(self)
