class Customer:
    all = []
    username_list = []
    def __init__(self, first_name, last_name, username) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        type(self).all.append(self)
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_first_name):
        if isinstance(new_first_name, str) and 1 <= len(new_first_name) <=30:
            self._first_name = new_first_name
        else:
            raise TypeError('First name must be str and cannot be blank!')
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        if isinstance(new_last_name, str) and 1 <= len(new_last_name) <=30:
            self._last_name = new_last_name
        else:
            raise TypeError('Last name must be str and cannot be blank!')
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if new_username not in type(self).username_list:
            if 1 >= len(new_username) or len(new_username) >= 30:
                raise TypeError('Please make sure your username is between 1 to 30 characters.')
            else: 
                type(self).username_list.append(new_username)
                self._username = new_username          
        else:
            raise TypeError('This username has been taken, please choose another one.')
            
        
    def game_list(self):
        game_list = []
        for transaction in Transaction.all:
            if transaction.game not in game_list:
                game_list.append(transaction.game)
        return game_list
    

from .transaction import Transaction