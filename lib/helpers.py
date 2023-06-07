import re
from simple_chalk import chalk, bold, underline
from classes.game import Game
from classes.user import User
from classes.review import Review

def welcome():
    print(bold(chalk.red("Welcome to 'Game Store'!")))

def menu():
    print(underline(chalk.yellow("""
    Please type in the number corresponding to the choice.
    """)))
    print(chalk.green('1. All Games'))
    print(chalk.green("2. Find Games by Game's name"))
    print(chalk.green('3. Find Games by Genres'))
    print(chalk.green('4. New Games for 2023'))
    print(chalk.green('5. Add Review to Game'))
    print(chalk.green('6. Done'))

def review_tab():
    print(underline(chalk.yellow("""
    Please type in the number corresponding to the choice.
    """)))
    print(chalk.green('1. Add Review'))
    print(chalk.green('2. Back'))

def login():
    print(underline(chalk.yellow("""
    Please login in to add a review.
    """)))
    print(chalk.green('1. Existing User'))
    print(chalk.green('2. New User'))
    print(chalk.green('3. Back'))

def create_user():
    first_name = input(chalk.yellow('Please enter your first name: '))
    last_name = input(chalk.yellow('Please enter your last name: '))
    try:
        user = User.create_user(first_name, last_name)
        print(user)
    except Exception as e:
        print(bold(chalk.red('Failed to create user: ')), e)
    
def existing_user():
    first_name = input(chalk.yellow('Please enter your first name: '))
    last_name = input(chalk.yellow('Please enter your last name: '))
    user = User.find_by_user(first_name, last_name)
    print(user) if user else print(bold(chalk.red('No user found')))

def find_by_name():
    name = input(chalk.yellow('Please type the game name.'))
    filtered = [game for game in Game.all if game.name is name]
    for game in filtered:
        print(game)