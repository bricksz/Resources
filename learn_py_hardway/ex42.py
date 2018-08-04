'''
+++ GOTHONS ARE GETTING CLASSY +++

'''

class TheThing(object):

    def __init__(self):           # __init__ sets up python class with internal variables.
        self.number = 0

    def some_function(self):
        print("I got called.")

    def add_me_up(self, more):
        self.number += more
        return self.number

'''
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print(a.add_me_up(20))
print(a.add_me_up(20))
print(b.add_me_up(30))
print(b.add_me_up(30))
print("\n")
print(a.number)
print(b.number)
'''

from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud. If she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better than this."
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print("\n------------")
            room = getattr(self, next)
            next = room()

    def death(self):
        print(self.quips[randint(0, len(self.quips)-1)])
        exit(1)

    def central_corridor(self):
        print("HUGE WALL OF MMORPH TEXT, you have a gun, what do you do?")

        action = input("> ")

        if action == "shoot!":
            print("STUFF HAPPENS AND UR DEAD")
            return 'death'

        elif action == 'dodge!':
            print('STUFF HAPPENS AND UR DEAD')
            return 'death'

        elif action == "tell a joke":
            print('U GOT LUCKY')
            return 'laser_weapon_armory'

        else:
            print('DOES NOT COMPUTE!')
            return 'central_corridor'

    def laser_weapon_armory(self):
        print('TEXT TEXT TEXT\n The code is 3 didgits, 1 or 2 selection only.')
        code = "%d%d%d" % (randint(1,2), randint(1,2), randint(1,2))
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:
            print('BZZZZZZZED!')
            guesses += 1
            guess = input('[keypad]>')

        if guess == code:
            print('OPEN')
            return 'the_bridge'

        else:
            print('DEAD')
            return 'death'

    def the_bridge(self):
        print('BOMB SCENE, WHAT DO YOU DO?')

        action = input("> ")

        if action == "throw the bomb":
            print('DEAD')
            return 'death'

        elif action == 'slowly place the bomb':
            print('BOMB IS OFF')
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

    def escape_pod(self):
        print('2 PODS, CHOOSE ONE')

        good_pod = randint(1,2)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print('You jump into pod %s' % guess)
            print('but your dead')
            return 'death'

        else:
            print('You jump into pod %s' % guess)
            print('ESCAPE!')
            exit(0)

a_game = Game('central_corridor')
a_game.play()

