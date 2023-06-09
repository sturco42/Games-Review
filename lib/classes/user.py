from classes.__init__ import CONN, CURSOR

class User:

    def __init__(self, first_name, last_name, username, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.id = id

    def __repr__(self):
        return f"<First Name: {self.first_name} | Last Name: {self.last_name} | Username: {self.username}>"

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
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 1 <= len(new_username) <=30:
            self._username = new_username
        else:
            raise Exception('The last name must be a string between 1 to 30 characters.')

            
    def save(self):
        CURSOR.execute("""
            INSERT INTO users (first_name, last_name, username)
            VALUES ( ?, ?, ?)
        """, (self.first_name, self.last_name, self.username))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def all(cls):
        CURSOR.execute("""
            SELECT * FROM users;
        """)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def create_user(cls, first_name, last_name, new_username):
        all_username = [user.username for user in cls.all()]
        if new_username not in all_username:
            new_user = cls(first_name, last_name, new_username)
            new_user.save()
            return new_user
        else:
            raise TypeError('This username has been taken. Please pick another one.')

    @classmethod
    def find_by_user(cls, username):
        CURSOR.execute("""
           SELECT * FROM users
           WHERE username == ?
        """, (username, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0])
