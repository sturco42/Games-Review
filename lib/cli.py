from classes.game import Game
from classes.user import User
from classes.review import Review
from classes.__init__ import CONN, CURSOR
from simple_chalk import chalk, bold, underline

import time

from helpers import (
    welcome,
    menu,
    review_tab,
    login,
    create_user,
    existing_user,
    find_by_name,
)

def main():
    welcome()

    # choice = 0
    while True :#choice != 0: 
        time.sleep(2)
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
            review_tab()
            choice_2 = input()
            if choice_2 == '1':
                login()
                choice_3 = input()
                if choice_3 == '1':
                    existing_user()
                if choice_3 == '2':
                    create_user()
                if choice_3 == '3':
                    print('')
                else:
                    print(bold(chalk.red('Please type vaild number.')))
            if choice_2 == '2':
                menu()
                #Trying to avoid previous input...
                #break
            else:
                print(bold(chalk.red('Please type vaild number.')))
        if choice == '6':
            print("See you next time!")
            break
        else:
            print(bold(chalk.red('Please type vaild number.')))


        



if __name__ == '__main__':
    main()