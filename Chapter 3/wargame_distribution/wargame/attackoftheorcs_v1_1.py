from __future__ import print_function
"""ch01_ex03_AbstractBaseClass

A text-based game to acquire a hut by defeating the enemy (OOP- using  ABC).

This module is compatible with Python 3.5.x. It contains
supporting code for the book, Learning Python Application Development,
Packt Publishing.

Demonstrates use of Abstract Base Class (ABC) in Python. It is a hint
to an EXERCISE of Chapter 1.

The player inputs a hut number. If the occupant is an enemy, the player is
given an option to 'attack'. Player wins if he defeats the enemy.
Additionally,the player can 'run away' from the combat, get healed
in friendly hut and then resume the fight.

In the aforementioned book this is also referred to as
"Attack of the Orcs v1.0.0". More details can be found in the relevant
chapter of the book..

RUNNING THE PROGRAM:
--------------------
- Python 3.5.x must be installed on your system.
- It is assumed that you have Python 3.5 available in your environment
  variable PATH. It will be typically available as 'python' or 'python3'.
- Here is the command to execute this code from command prompt

        $ python ch01_ex03_AbstractBaseClass.py
        ( OR $ python3 ch01_ex03_AbstractBaseClass.py)

- See the README file for more information. Or visit python.org for OS
  specific instructions on executing Python from a command prompt.

.. seealso:: ch01_ex03.py -- Same example without using ABC

.. todo::

1. The code comments and function descriptions in this file are
   intentionally kept to a minimum! See a later chapter of the book to
   learn about the code documentation and best practices!
   Feel free to add documentation after reading that chapter.
   Description of the code can be found in the book.
2. Split the code into smaller modules
3. See the other TODO comments..things you can try fixing as an exercise!

:copyright: 2016, Ninad Sathaye

:license: The MIT License (MIT) . See LICENSE file for further details.
"""
import random
import textwrap
import sys
from abc import ABCMeta, abstractmethod
from gameuniterror import GameUnitError
from gameutils import print_bold, weighted_random_selection
from abstractgameunit import AbstractGameUnit
from knight import Knight
from hut import Hut


if sys.version_info < (3, 0):
    print("This code requires Python 3.x and is tested with version 3.5.x ")
    print("Looks like you are trying to run this using " + 
    "Python version: {}.{} ".format(sys.version_info[0], sys.version_info[1]))
    print("Exiting...")
    sys.exit(1)


class OrcRider(AbstractGameUnit):
    """Class that represents the game character Orc Rider"""
    def __init__(self, name=''):
        super().__init__(name=name)
        self.max_hp = 30
        self.health_meter = self.max_hp
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        """Print basic information about this character"""
        print("Grrrr..I am an Orc Wolf Rider. Don't mess with me.")




class AttackOfTheOrcs:
    """Main class to play Attack of The Orcs game"""
    def __init__(self):
        self.huts = []
        self.player = None

    def get_occupants(self):
        """Return a list of occupant types for all huts.

        .. todo::

             Prone to bugs if self.huts is not populated.
             Chapter 2 talks about catching exceptions
        """
        return [x.get_occupant_type() for x in self.huts]

    def show_game_mission(self):
        """Print the game mission in the console"""
        print_bold("Mission:")
        print("  1. Fight with the enemy.")
        print("  2. Bring all the huts in the village under your control")
        print("---------------------------------------------------------\n")

    def _process_user_choice(self):
        """Process the user input for choice of hut to enter"""
        verifying_choice = True
        idx = 0
        print("Current occupants: {}".format(self.get_occupants()))
        
        while verifying_choice:
            user_choice = input("Choose a hut number to enter (1-5): ")
            try:
                idx = int(user_choice)
            except ValueError as e:
                print("Invalid input, args: {}\n".format(e.args))
                continue
            try:
                if self.huts[idx-1].is_acquired:
                    print("You have already acquired this hut. Try again."
                     "<INFO: You can NOT get healed in already acquired hut.>")
                else:
                    verifying_choice = False
            except IndexError:
                print("Invalid input : {}".format(idx))
                print("Number should be in the range 1-5. Try again")
                continue
        return idx

    def _occupy_huts(self):
        """Randomly occupy the huts with one of: friend, enemy or 'None'"""
        for i in range(5):
            choice_lst = ['enemy', 'friend', None]
            computer_choice = random.choice(choice_lst)
            if computer_choice == 'enemy':
                name = 'enemy-{}'.format(str(i+1))
                self.huts.append(Hut(i+1, OrcRider(name)))
            elif computer_choice == 'friend':
                name = 'knight-{}'.format(str(i+1))
                self.huts.append(Hut(i+1, Knight(name)))
            else:
                self.huts.append(Hut(i+1, computer_choice))

    def play(self):
        """Workhorse method to play the game.

        Controls the high level logic to play the game. This is called from
        the main program to begin the game execution.
        """
        self.player = Knight()
        self._occupy_huts()
        acquired_hut_counter = 0
        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquired_hut_counter < 5:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])
            if self.player.health_meter <= 0:
                print_bold("YOU LOSE  :(  Better luck next time")
                break
            if self.huts[idx-1].is_acquired:
                acquired_hut_counter += 1

        if acquired_hut_counter == 5:
            print_bold("Congratulations! YOU WIN!!!")


if __name__ == '__main__':
    game = AttackOfTheOrcs()
    game.play()
