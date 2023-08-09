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
        EXAMINATION: '',
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
        EXAMINATION: '',
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
        EXAMINATION: '',
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