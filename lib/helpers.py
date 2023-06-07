import re
from simple_chalk import chalk, bold, underline
from classes.game import Game
from classes.customer import Customer
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
    print(chalk.green('4. Top 10 Games'))
    print(chalk.green('5. New Games for 2023'))
    print(chalk.green('6. Add Review to Game'))
    print(chalk.green('7. Done'))

def review_tab():
    print(underline(chalk.yellow("""
    Please type in the number corresponding to the choice.
    """)))
    print('1. Add Review')
    print('2. Back')

def login():
    print(chalk.yellow("""
    Please login in to add a review.
    """))
    print('1. Exiting Customer')
    print('2. New Customer')
    print('3. Back')

def create_customer():
    first_name = input(chalk.yellow('Please enter your first name: '))
    last_name = input(chalk.yellow('Please enter your last name: '))
    username = input(chalk.yellow('Please enter your username: '))
    try:
        customer = Customer.create_customer(first_name, last_name, username)
        print(customer)
    except Exception as e:
        print('Failed to create customer: ', e)
    

def exiting_customer():
    username = input(chalk.yellow('Please enter your username: '))
    customer = Customer.find_by_username(username)
    print(customer) if customer else print('No customer found')

def find_by_name():
    name = input(chalk.yellow('Please type the game name.'))
    filtered = [game for game in Game.all if game.name is name]
    for game in filtered:
        print(game)