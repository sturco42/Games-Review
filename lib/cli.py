from classes.game import Game
from classes.customer import Customer
from classes.review import Review
from classes.__init__ import CONN, CURSOR
from simple_chalk import chalk, bold, underline

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

    # choice = 0
    while True :#choice != 0: 
        time.sleep(3)
        menu()
        choice = input()

        if choice == '1':
            print(' Id    Title    Publisher    Year')
            for game in Game.all():
                print(game)

        if choice == '2':
            title = input(chalk.yellow('Please enter the game title: '))
            game = Game.find_by_title(title)
            print(f"""
                Title: {game.title}
                Publisher: {game.publisher}
                Year: {game.year}
                Ave Rating: {game.ave_rating}
            """)

        if choice == '3':
            print('working on ...')

        if choice == '4':
            print('working on ...')

        if choice == '5':
            print('working on ...')

        if choice == '6':
            review_tab()
            choice_2 = input()
            if choice_2 == '1':
                login()
                choice_3 = input()
                if choice_3 == '1':
                    exiting_customer()
                if choice_3 == '2':
                    create_customer()
                if choice_3 == '3':
                    review_tab()
                else:
                    print(bold(chalk.red('Please type vaild number.')))
            if choice_2 == '2':
                menu()
            else:
                print(bold(chalk.red('Please type vaild number.')))
        if choice == '7':
            print("See you next time!")
            break
        else:
            print(bold(chalk.red('Please type vaild number.')))


        



if __name__ == '__main__':
    main()