from .__init__ import CONN, CURSOR

class Customer:

    all = []
    def __init__(self, first_name, last_name, username, customer_id = None):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        # self.id = id
        type(self).all.append(self)
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_first_name):
        if isinstance(new_first_name, str) and 1 <= len(new_first_name) <=30:
            self._first_name = new_first_name
        else:
            raise TypeError('The first name must be a string between 1 to 30 characters.')
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        if isinstance(new_last_name, str) and 1 <= len(new_last_name) <=30:
            self._last_name = new_last_name
        else:
            raise TypeError('The last name must be a string between 1 to 30 characters.')
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        username_list = [customer.username for customer in type(self).all]
        if new_username not in username_list:
            if 1 >= len(new_username) or len(new_username) >= 30:
                raise TypeError('The username must be a string between 1 to 30 characters.')
            else: 
                username_list.append(new_username)
                self._username = new_username          
        else:
            raise TypeError('This username has been taken, please choose another one.')
    
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                username TEXT
            )
        """)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("""
            DROP TABLE IF EXISTS customers
        """)
        CONN.commit()   

    def save(self):
        CURSOR.execute("""
            INSERT INTO customers (first_name, last_name, username)
            VALUES ( ?, ?, ?)
        """, (self.first_name, self.last_name, self.username))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create_customer(cls, first_name, last_name, username):
        new_customer = cls(first_name, last_name, username)
        new_customer.save()
        return new_customer

    @classmethod
    def find_by_username(cls, username):
        CONN.execute("""
           SELECT * FROM customers
           WHERE username == ?
        """, (username,))
        row = CONN.fetchone()
        return Customer(row[1], row[2], row[3], row[0]) if row else None

