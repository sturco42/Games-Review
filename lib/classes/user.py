from classes.__init__ import CONN, CURSOR

class User:

    def __init__(self, first_name, last_name, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        if isinstance(new_first_name, str) and 1 <= len(new_first_name) <=30:
            self._first_name = new_first_name
        else:
            raise Exception('The first name must be a string between 1 to 30 characters.')

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        if isinstance(new_last_name, str) and 1 <= len(new_last_name) <=30:
            self._last_name = new_last_name
        else:
            raise Exception('The last name must be a string between 1 to 30 characters.')
    
    @property
    def username(self):
        return self._username
            
    def save(self):
        CURSOR.execute("""
            INSERT INTO users (first_name, last_name)
            VALUES ( ?, ?)
        """, (self.first_name, self.last_name))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create_user(cls, first_name, last_name):
        new_user = cls(first_name, last_name)
        new_user.save()
        return new_user

    @classmethod
    def find_by_user(cls, first_name, last_name):
        CONN.execute("""
           SELECT * FROM users
           WHERE first_name == ?
           WHERE last_name == ?
        """, (first_name, last_name, ))
        row = CONN.fetchone()
        return User(row[1], row[2], row[0]) if row else None

