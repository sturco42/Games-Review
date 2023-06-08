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
    print(chalk.green("2. Search Games"))
    # print(chalk.green('3. Find Games by Genres'))
    print(chalk.green('3. New Releases'))
    print(chalk.green('4. Add Review'))
    print(chalk.green('5. Done'))

def review_tab():
    print(underline(chalk.yellow("""
    Please type in the number corresponding to the choice.
    """)))
    print(chalk.green('1. Add Review'))
    print(chalk.green('2. Back'))

def login():
    print(underline(chalk.yellow("""
    Please login first.
    """)))
    print(chalk.green('1. Existing User'))
    print(chalk.green('2. New User'))

def create_user():
    first_name = input(chalk.yellow('Please enter your first name: '))
    last_name = input(chalk.yellow('Please enter your last name: '))
    username = input(chalk.yellow('Please enter your username: '))
    try:
        user = User.create_user(first_name, last_name, username)
        print(user)
        add_review(user.id)
    except Exception as e:
        print(bold(chalk.red('Failed to create user: ')), e)
    
def existing_user():
    username = input(chalk.yellow('Please enter your username: '))
    try:
        user = User.find_by_user(username)
        print(user)
        add_review(user.id)
    except Exception as e:
        print(bold(chalk.red('No user found!')))

def game_details(title):
    game = Game.find_by_title(title)
    try:
        print(f"""
            Title: {game.title}
            Publisher: {game.publisher}
            Year: {game.year}
            Ave Rating: {Game.ave_rating(game.id)}
        """)
    except:
        print(bold(chalk.red('There is no such game.')))

def game_details_by_id(id):
    game = Game.find_by_game_id(id)
    try:
        print(f"""
            Title: {game.title}
            Publisher: {game.publisher}
            Year: {game.year}
            Ave Rating: {Game.ave_rating(id)}
        """)
    except:
        print(bold(chalk.red('There is no such game.')))

def add_review(id):
    game_id = input(chalk.yellow('What is the game id: '))
    rating = input(chalk.yellow('Please rate from 1-10: '))
    Review.create_review(int(rating), game_id, id)
    