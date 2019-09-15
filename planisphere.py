from sys import exit
from random import randint
from textwrap import dedent


class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    @property
    def hint(self):
        return "Possible variants are: "  + ", ".join([i for i in self.paths])

def load_room(map, name):
    return map.get(name)


def name_room(map, room):
    for key, value in map.items():
        if value == room:
            return key


quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

START = 'central_corridor'

rooms = {
    'central_corridor': Room("Central corridor",

                            """
    The Gothons of Planet Percal #25 have invaded your ship
    destroyed your entire crew. You are the last surviving
    member and your last mission is to get the neutron destruction
    bomb from the Weapons Armory, put it in the bridge, and
    blow the ship up after getting into an escape pod.

    You're running down the central corridor to the Weapons
    Armory when a Gothon jumps out, red scaly skin, dark grim
    teeth, and evil clown costume flowing around his hate
    filled body. He's blocking the door to the Armory and
    about to pull a weapon to blast you.
                            
                            """),

    'laser_weapon_armory': Room("Laser Weapon Armory",
                            """
    Lucky for you they made you learn Gothon insults in the academy. You
    tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvg
    nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
    not to laugh, then busts out laughing and can't move. While he's
    laughing you run up and shoot him square in the head putting him down,
    then jump through the Weapon Armory door.
    
    You do a dive roll into the Weapon Armory, crouch and scan the room fo
    more Gothons that might be hiding. It's dead quiet, too quiet. You
    stand up and run to the far side of the room and find the neutron bomb
    in its container. There's a keypad lock on the box and you need the
    code to get the bomb out. If you get the code wrong 10 times then the
    lock closes forever and you can't get the bomb. The code is 3 digits.
                            """),

    'the_bridge': Room("The Bridge",
                            """
    The container clicks open and the seal breaks, letting gas out. You
    grab the neutron bomb and run as fast as you can to the bridge where you
    must place it in the right spot.
    
    You burst onto the Bridge with the netron destruct bomb under your arm
    and surprise 5 Gothons who are trying to take control of the ship. Each
    of them has an even uglier clown costume than the last. They haven't
    pulled their weapons out yet, as they see the active bomb under your arm
    and don't want to set it off.
                            """),

    'escape_pod': Room("Escape Pod",
                            """
    You point your blaster at the bomb under your arm and the Gothons put
    their hands up and start to sweat. You inch backward to the door, open
    it, and then carefully place the bomb on the floor, pointing your
    blaster at it. You then jump back through the door, punch the close
    button and blast the lock so the Gothons can't get out. Now that the
    bomb is placed you run to the escape pod to get off this tin can.
    
    You rush through the ship desperately trying to make it to
    pod before the whole ship explodes. It seems like hardly any gothon
    are on the ship, so your run is clear of interference. You have
    chamber with the escape pods, and now need to pick one to take. Some of
    them could be damaged but you don't have time to look. There's
    which one do you take?
                            """),

    'the_end_winner': Room("The End",
                            """
    You jump into pod 2 and hit the eject button. The pod easily
    into space heading to the planet below. As it flies to the   . You
    look back and see your ship implode then explode like a bright
    taking out the Gothon ship at the same time. You won!
                            """),

    'the_end_loser': Room("The End",
                            """
    You jump into a random pod and hit the eject button. The pod escapes
    out into the void of space, then implodes as the hull ruptures, crushing
    your body into jam jelly.
                        """),

    'generic_death': Room("death", quips[randint(0, len(quips) - 1)])
}

rooms['central_corridor'].add_paths({
    'shoot!': rooms.get('generic_death'),
    'dodge!': rooms.get('generic_death'),
    'tell a joke': rooms.get('laser_weapon_armory')
})

rooms['escape_pod'].add_paths({
    '2': rooms.get('the_end_winner'),
    '*': rooms.get('the_end_loser')
})

rooms['the_bridge'].add_paths({
    'throw the bomb': rooms.get('generic_death'),
    'slowly place the bomb': rooms.get('escape_pod')
})

rooms['laser_weapon_armory'].add_paths({
    '0132': rooms.get('the_bridge'),
    '*': rooms.get('generic_death')
})
