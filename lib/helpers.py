import re
import chalk
from classes.game import Game
from classes.customer import Customer
from classes.review import Review

def welcome():
    print(chalk.bold.bggreen("Welcome to 'Game Store'!"))

def menu():
    print(chalk.italic.yellow("""
    Please type in the number corresponding to the choice.
    """))
    print('1. All Games')
    print("2. Find Games by Game's name")
    print('3. Find Games by Genres')
    print('4. Top 10 Games')
    print('5. New Games for 2023')
    print('6. Add Review to Game')

def review_tab():
    print(chalk.italic.yellow("""
    Please type in the number corresponding to the choice.
    """))
    print('1. Add Review')
    print('2. Back')

def login():
    print(chalk.italic.yellow("""
    Please login in to add a review.
    """))
    print('1. Exiting Customer')
    print('2. New Customer')
    print('3. Back')

def create_customer():
    first_name = input(chalk.italic.yellow('Please enter your first name: '))
    last_name = input(chalk.italic.yellow('Please enter your last name: '))
    username = input(chalk.italic.yellow('Please enter your username: '))
    try:
        customer = Customer.create(first_name, last_name, username)
        print(customer)
    except Exception as e:
        print('Failed to create customer:', e)
    

def exiting_customer():
    username = input(chalk.italic.yellow('Please enter your username'))

def find_by_name():
    name = input(chalk.italic.yellow('Please type the game name.'))
    filtered = [game for game in Game.all if game.name is name]
    for game in filtered:
        print(game)