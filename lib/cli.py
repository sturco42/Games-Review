from classes.game import Game
from classes.customer import Customer
from classes.review import Review
from classes.__init__ import CONN, CURSOR

import time

from helpers import (
    welcome,
    menu,
    review_tab,
    login,
    create_customer,
    exiting_customer,
    find_by_name,
)

def main():
    welcome()

    choice = 0
    while choice != 9:
        time.sleep(5)
        print("""
            Please type in the number corresponding to the choice.
            ______________________________________________________
        """)
        menu()
        choice = int(input())

        if choice == 1:
            print('')
            for game in Game.all:
                print(game)

        if choice == 2:
            find_by_name()

        if choice == 3:
            print('working on ...')

        if choice == 4:
            print('working on ...')

        if choice == 5:
            print('working on ...')

        if choice == 6:
            review_tab()
            if choice == 1:
                login()
                if choice == 1:
                    exiting_customer()
                if choice == 2:
                    create_customer()
                if choice == 3:
                    review_tab()
                else:
                    print('Please type vaild number.')
            if choice == 2:
                menu()
            else:
                print('Please type vaild number.')
        else:
            print('Please type vaild number.')


        



if __name__ == '__main__':
    main()