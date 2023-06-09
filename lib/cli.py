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
        elif choice == '3':
            if Game.find_by_year('2020'):
                for game in Game.find_by_year('2020'):
                    print (game)
                id = input(chalk.yellow('Please enter the game id to see the details: '))
                game_details_by_id(id)
            else: 
                print('Sorry, cannot find any game.')
        elif choice == '4':
            Game.highest_rated_games()
        elif choice == '5':
            login()
            choice_2 = input()
            if choice_2 == '1':
                existing_user()
            elif choice_2 == '2':
                create_user()
            elif choice_2 == '3':
                print("Back to main menu.")
            else:
                print(bold(chalk.red('Please type a valid number.')))
        elif choice == '6':
            print("See you next time!")
            break
        else:
            print(bold(chalk.red('Please type a valid number.')))

if __name__ == '__main__':
    main()