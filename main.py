#### A text adventure game written using Python3 ####

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100



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
myPlayer = Player()



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
myBoss = Boss()



#### Inventory System ####

class Item:
    def __init__(self):
        self.name = ''
        self.description = ''
        self.amount = 0
        self.atk = 0
myItem = Item()

class Inventory:
    def __init__(self):
        self.capacity = 0
        self.items = []

    def show(self):
        index = 1
        for item in self.items:
            print(str(f'{index} -> [x{Item.amount}] {Item.name}'))
            index += 1
myInventory = Inventory()



#### Items ####

sword = Item('Sword', 'A sword used by a knight.', 1, 10)



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
        print('Please enter a valid command')
        option = input('> ')
        if option.lower() == ('play'):
            setup_game()
        elif option.lower() == ('help'):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()

def title_screen():
    os.system('cls')
    print('####################################')
    print('# Welcome to the castle of KelSax! #')
    print('####################################')
    print('              ~ Play ~              ')
    print('              ~ Help ~              ')
    print('              ~ Quit ~              ')
    title_options()

def help_menu():
    os.system('cls')
    print('####################################')
    print('#               Help               #')
    print('####################################')
    print('#                                  #')
    print('####################################')
    print('#    A Python3 dungeon text RPG    #')
    print('#         Created by: AEM          #')
    print('#         Copyrighted 2023         #')
    print('####################################')
    title_options()                     #')



#### Map ####

"""
#### Player starts at d3 ####
^^^^^^^^^^^^^^^^^^^
[a1] [a2] [a3] [a4]
     |\ |
[b1] [b2] [b3] [b4]
     |\ |
[c1] [c2] [c3] [c4]
     |\ |
[d1] [d2] [d3] [d4]
|\ |           
[e1] [e2] [e3] [e4]
"""

ZONENAME = ''
DESCRIPTION = ''
EXAMINATION = ''
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
RIGHT = 'right', 'east'
LEFT = 'left', 'west'

solved_locations = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False,
    'e1': False, 'e2': False, 'e3': False, 'e4': False
}

zonemap = {
    'a1': {
        ZONENAME: 'West Tower',
        DESCRIPTION: 'You are in the West Tower of Kelsax.',
        EXAMINATION: 'You look out into the vast wasteland that is the desolated kingdom of Cantonia.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT:'a2',
        LEFT: ''
    },
    'a2': {
        ZONENAME: 'Rampart - West',
        DESCRIPTION: 'You stand upon the west most rampart.',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        RIGHT: 'a1',
        LEFT: 'a3'
    },
    'a3': {
        ZONENAME: 'Rampart - East',
        DESCRIPTION: 'You stand upon the east most rampart.',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: 'a2',
        LEFT: 'a4'
    },
    'a4': {
        ZONENAME: 'East Tower',
        DESCRIPTION: 'You are in the East Tower of Kelsax.',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: 'a3'
    },
    'b1': {
        ZONENAME: 'Guest Room - West',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: 'b2',
        LEFT: ''
    },
    'b2': {
        ZONENAME: 'Hallway/Staircase',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        RIGHT: 'b1',
        LEFT: 'b3'
    },
    'b3': {
        ZONENAME: 'Hallway',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: 'b2',
        LEFT: 'b4'
    },
    'b4': {
        ZONENAME: 'Guest room - East',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: 'b3'
    },
    'c1': {
        ZONENAME: 'Throne Room',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: 'c2',
        LEFT: ''
    },
    'c2': {
        ZONENAME: 'Hallway/Staircase',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: 'b1',
        DOWN: 'd1',
        RIGHT: 'c3',
        LEFT: 'c1'
    },
    'c3': {
        ZONENAME: 'Dinning Room',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: 'c4',
        LEFT: 'c2'
    },
    'c4': {
        ZONENAME: 'Ballroom',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: 'c3'
    },
    'd1': {
        ZONENAME: 'Dungeon Entrance',
        DESCRIPTION: '',
        EXAMINATION: 'There is a staircase leading down. An ominous aura surronds it.',
        SOLVED: False,
        UP: '',
        DOWN: 'e1',
        RIGHT: 'd2',
        LEFT: ''
    },
    'd2': {
        ZONENAME: 'Hallway/Staircase',
        DESCRIPTION: 'A hallway with a staircase leading up.',
        EXAMINATION: '',
        SOLVED: False,
        UP: 'c2',
        DOWN: '',
        RIGHT: 'd3',
        LEFT: 'd2'
    },
    'd3': {
        ZONENAME: 'Foyer',
        DESCRIPTION: 'You stand in the entry way to the caslte of Kelsax.',
        EXAMINATION: 'There are passages to the left and right of you.',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: 'd4',
        LEFT: 'd2'
    },
    'd4': {
        ZONENAME: 'Guard Room',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: 'e4',
        RIGHT: '',
        LEFT: 'd3'
    },
    'e1': {
        ZONENAME: 'Dungeon - Exit',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: 'd1',
        DOWN: '',
        RIGHT: '',
        LEFT: ''
    },
    'e2': {
        ZONENAME: 'Dungeon',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: 'e3',
        LEFT: 'e1'
    },
    'e3': {
        ZONENAME: 'Dungeon',
        DESCRIPTION: '',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: 'e4',
        LEFT: 'e2'
    },
    'e4': {
        ZONENAME: 'Lucius Tavien\'s Quarters',
        DESCRIPTION: 'Here stands the undead wizard Lucius Tavien.',
        EXAMINATION: '',
        SOLVED: False,
        UP: '',
        DOWN: '',
        RIGHT: '',
        LEFT: 'e3'
    }
}



#### Game Interactivity ####

def print_location():
    #print('\n' + ('#' * (4 + len(myPlayer.location))))
    #print('# ' + myPlayer.location + ' #')
    print(zonemap[myPlayer.location][ZONENAME])
    print(zonemap[myPlayer.location][DESCRIPTION])
    #print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print('\n')
    print('What would you like to do?')

    action = input('> ')
    acceptable_actions = [
        'move', 'go', 'travel', 'walk', 'quit', 'examine', 'interact', 'inspect', 'look', 'help', 'talk', 'fight', 'inventory'
    ]
    while action.lower() not in acceptable_actions:
        print('Unknown action.\n')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'interact', 'inspect', 'look']:
        player_examine(action.lower())
    elif action.lower() in ['inventory']:
        player_inventory(action.lower())



#### Movement ####

def player_move(myAction):
    ask = 'Where would you like to move to?\n'
    dest = input(ask)

    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handling(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handling(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handling(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handling(destination)

def movement_handling(destination):
    print('\n' + 'You have moved to the ' + destination + '.')
    myPlayer.location = destination
    print_location()



#### Examine ####

def player_examine(action):
    ask = 'Would you like to examine the room?\n'
    action = input(ask)

    if action in ['yes']:
        print(zonemap[myPlayer.location][EXAMINATION])
    elif action in ['no']:
        prompt()

    if zonemap[myPlayer.location][SOLVED] == True:
        print('You have cleared this room.')
    else:
        print('The mysteries of this room remain unsolved')



#### Inventory ####

def player_inventory():
    ask = 'Would you like to view your inventory?\n'
    action = input(ask)

    if action in ['yes']:
        print(myInventory.show())
    elif action in ['no']:
        prompt()



#### Game Functionality ####

def main_loop():

    while myPlayer.defeated or myBoss.defeated == False:
        prompt()

    if myBoss.defeated:
        victory = 'Congratulations! You have defeated the evil wizard that rules this castle!'

        for character in victory:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.30)

        sys.exit()

    elif myPlayer.defeated == True:
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
        time.sleep(0.10)

    player_name = input('> ')
    myPlayer.name = player_name

    question_job = 'What role do you play in this world?\n'
    question_job2 = 'Knight, Jester, or Mage?\n'

    for character in question_job:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)

    for character in question_job2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)

    player_job = input('> ')
    valid_jobs = ['knight', 'jester', 'mage']

    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print(player_name + ' traverses this world as a ' + player_job + '.\n')

    while player_job.lower() not in valid_jobs:
        player_job = input('> ')
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print(player_name + ' traverses this world as an: ' + player_job + '.\n')

    #### Player Classes ####

    if myPlayer.job == 'Knight':
        myPlayer.hp = 100
        myPlayer.mp = 25
        myPlayer.atk = 25
        myPlayer.df = 15
    elif myPlayer.job == 'Jester':
        myPlayer.hp = 75
        myPlayer.mp = 50
        myPlayer.atk = 20
        myPlayer.df = 10
    elif myPlayer.job == 'Mage':
        myPlayer.hp = 50
        myPlayer.mp = 100
        myPlayer.atk = 10
        myPlayer.df = 5


    #### Introduction ####

    os.system('cls')

    quest_intro = 'Welcome ' + player_name + ' the ' + player_job + ' to the castle of Kelsax!\n'

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
        time.sleep(0.30)

    os.system('cls')
    print('####################################')
    print('#       Your journey begins.       #')
    print('####################################')
    main_loop()

#### Initialize ####

title_screen()