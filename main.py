#### A text adventure game written using Python3 ####


#### Imports ####

import cmd
import textwrap
import sys
import os
import time
import random
from console import fg, bg, fx

from map import *
from items import ITEMS



#### Global Variables ####

WIDTH = 60
MARGIN = 3



#### Styling ####

def wrap(text):
    margin = MARGIN * " "
    paragraph = textwrap.fill(
        text,
        WIDTH,
        initial_indent=margin,
        subsequent_indent=margin,
    )
    
    print(paragraph)

def write(text):
    print(MARGIN * " ", text, sep="")

def header(title):
    print()
    write(fx.bold(title))
    print()



#### Player Setup ####

class Player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.atk = 0
        self.df = 0
        self.status_effects = {}
        self.location = 'd3'
        self.defeated = False
game_player = Player()

class Knight:
    def __init__(self):
        self.name = 'Knight'
        self.hp = 100
        self.mp = 25
        self.atk = 25
        self.df = 150
        self.inventory = {'Sword': 10}


#### Enemy Setup ####

class Boss:
    def __init__(self):
        self.name = 'Lucius Tavien'
        self.job = 'Undead Wizard'
        self.hp = 100
        self.mp = 100
        self.atk = 20
        self.df = 10
        self.location = 'e4'
        self.defeated = False
game_boss = Boss()



#### Inventory System ####

class Item:
    def __init__(self, name, description, amount, atk, df):
        self.name = name
        self.description = description
        self.amount = amount
        self.atk = atk
        self.df = df

    def add_inventory(self, inventory):
        if len(inventory.items) < inventory.capacity:
            inventory.items.append(self)
            wrap(f'x{self.amount} {self.name} added to your Inventory')
        else:
            wrap('No room for more items...')
item = Item('', '', 0, 0, 0)

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def __repr__(self):
        return self.items
    
    def show(self):
        index = 1
        for item in self.items:
            wrap(str(f'{index} -> [x{item.amount}] {item.name}'))
            index += 1
inventory = Inventory(5)



#### Title Screen ####

def title_options():
    option = input('> ')
    if option.lower() == ('play'):
        setup_game()
    elif option.lower() == ('help'):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        wrap('Please enter a valid command')
        option = input('> ')
        if option.lower() == ('play'):
            setup_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()

def title_screen():
    os.system('cls')
    wrap('####################################')
    wrap('# Welcome to the castle of KelSax! #')
    wrap('####################################')
    wrap('              ~ Play ~              ')
    wrap('              ~ Help ~              ')
    wrap('              ~ Quit ~              ')
    title_options()

def help_menu():
    os.system('cls')
    wrap('####################################')
    wrap('#               Help               #')
    wrap('####################################')
    wrap('#                                  #')
    wrap('####################################')
    wrap('#    A Python3 dungeon text RPG    #')
    wrap('#         Created by: AEM          #')
    wrap('#         Copyrighted 2023         #')
    wrap('####################################')
    title_options()                     #')



#### Game Interactivity ####

def print_location():
    #wrap('\n' + ('#' * (4 + len(my_player.location))))
    #wrap('# ' + game_player.location + ' #')
    wrap(zonemap[game_player.location][ZONENAME])
    wrap(zonemap[game_player.location][DESCRIPTION])
    #wrap('\n' + ('#' * (4 + len(game_player.location))))

def prompt():
    wrap('\n')
    wrap('What would you like to do?')

    action = input('> ')
    acceptable_actions = [
        'move', 'go', 'travel', 'walk', 'quit', 'examine', 'interact', 'inspect', 'look', 'help', 'talk', 'speak' 'fight', 'inventory', 'shop'
    ]
    while action.lower() not in acceptable_actions:
        wrap('Unknown action.\n')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine']:
        player_examine(action.lower())
    elif action.lower() in ['interact', 'inspect', 'look']:
        player_interact()
    elif action.lower() in ['shop']:
        game_shop(action.lower())
    elif action.lower() in ['inventory']:
        player_inventory(action.lower())



    #### Movement ####

def player_move(myAction):
    ask = 'Where would you like to move to?\n'
    dest = input(ask)

    if dest in ['up', 'north']:
        destination = zonemap[game_player.location][UP]
        movement_handling(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[game_player.location][DOWN]
        movement_handling(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[game_player.location][RIGHT]
        movement_handling(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[game_player.location][LEFT]
        movement_handling(destination)

def movement_handling(destination):
    wrap('\n' + 'You have moved to the ' + destination + '.')
    game_player.location = destination
    print_location()



    #### Examine ####

def player_examine(action):
    ask = 'Would you like to examine the room?\n'
    action = input(ask)

    if action in ['yes']:
        wrap(zonemap[game_player.location][EXAMINATION])
    elif action in ['no']:
        prompt()

    if zonemap[game_player.location][SOLVED] == True:
        wrap('You have cleared this room.')
    else:
        wrap('The mysteries of this room remain unsolved')



    #### Interact ####

def player_interact(action):
    ask = 'Would you like to inspect the room?\n'
    action = input(ask)

    if action in ['yes']:
        wrap(zonemap[game_player.location][ITEMS])
    elif action in ['no']:
        prompt()


    #### Shop ####

def game_shop(action):
    ask = 'Would you like to examine the room?\n'
    action = input(ask)

    if action in ['yes']:
        wrap("\nItems for sale.\n")
        for item in ITEMS.values():
            wrap(f'{item["name"]:<13}  {item["description"]}')
    elif action in ['no']:
        prompt()



    #### Inventory ####

def player_inventory(action):
    ask = 'Would you like to view your inventory?\n'
    action = input(ask)

    if action in ['yes']:
        wrap(str(inventory.items))
    elif action in ['no']:
        prompt()



#### Game Functionality ####

def main():

    while game_player.defeated == False and game_boss.defeated == False:
        prompt()

    if game_boss.defeated == True:
        victory = 'Congratulations! You have defeated the evil wizard that rules this castle!'

        for character in victory:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.30)

        sys.exit()

    elif game_player.defeated == True:
        defeat = 'You have lost the battle and have died!'

        for character in defeat:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.30)

        sys.exit()

    

def setup_game():
    os.system('cls')

    #### Character Creation ####

    question_name = 'Hello traveler, what is your name?\n'

    for character in question_name:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    player_name = input('> ')
    game_player.name = player_name

    question_job = 'What role do you play in this world?\n'
    question_job2 = 'Knight, Noble, or Astrologist?\n'

    for character in question_job:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    for character in question_job2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    player_job = input('> ')
    valid_jobs = ['knight', 'noble', 'astrologist']

    if player_job.lower() in valid_jobs:
        game_player.job = player_job
        wrap(player_name + ' traverses this world as a ' + player_job + '.\n')

    while player_job.lower() not in valid_jobs:
        player_job = input('> ')
        if player_job.lower() in valid_jobs:
            game_player.job = player_job
            wrap(player_name + ' traverses this world as an: ' + player_job + '.\n')

    #### Player Classes ####

    if game_player.job == Knight:
        game_player.hp = 100
        game_player.mp = 25
        game_player.atk = 25
        game_player.df = 15
        '''sword = Item('Sword', 'A sword used by a knight.', 1, 10, 0)
        sword.add_inventory(inventory)'''


    elif game_player.job == 'Noble':
        game_player.hp = 75
        game_player.mp = 50
        game_player.atk = 20
        game_player.df = 10


    elif game_player.job == 'Astrologist':
        game_player.hp = 50
        game_player.mp = 100
        game_player.atk = 10
        game_player.df = 5



    #### Introduction ####

    os.system('cls')

    '''quest_intro = 'Welcome ' + player_name + ' the ' + player_job + ' to the castle of Kelsax!\n'

    for character in quest_intro:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    
    speech1 = 'You begin your journey in the foyer of the castle.\n'
    speech2 = 'There is no one around you.\n'
    speech3 = '...Initializing...'

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)

    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)

    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.30)'''

    os.system('cls')
    wrap('####################################')
    wrap('#       Your journey begins.       #')
    wrap('####################################')
    main()

#### Initialize ####

if __name__ == "__main__":
    title_screen()