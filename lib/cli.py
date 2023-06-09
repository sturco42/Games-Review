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
    game_details,
    game_details_by_id
)

def main():
    welcome()
    time.sleep(2)
    while True :
        menu()
        choice = input()
        if choice == '1':
            for game in Game.all():
                print(game)
            id = input(chalk.yellow('Please enter the game id to see the details: '))
            game_details_by_id(id)

        elif choice == '2':
            title = input(chalk.yellow('Please enter the game title: '))
            game_details(title)

        # if choice == '3':
        #     print('working on ...')

        elif choice == '3':
            print(Game.find_by_year('2020')) if Game.find_by_year('2020') else print('Sorry, cannot find any game.')

        elif choice == '4':
            login()
            choice_2 = input()
            if choice_2 == '1':
                existing_user()
            elif choice_2 == '2':
                create_user()
            elif choice_2 == '3':
                print("Back to main menu.")
            else:
                print(bold(chalk.red('Please type cool number.')))
        elif choice == '5':
            print("See you next time!")
            break
        else:
            print(bold(chalk.red('Please type valid number.')))


if __name__ == '__main__':
    main()