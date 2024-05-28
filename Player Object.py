#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     24/09/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Import random for the Gems function
import time
import random
import sys


# delclare all cariables and arrays
prompt = "\n>> "
keyLocation = ""
playerLocation = ""
locations = ["east", "west", "northeast", "northwest"]
class player:
    def _init_(self, name):

def invalidInput():
    delayPrint("\nInvalid Input")

def delayPrint(x):
    for i in x:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)

def key():
    global keyLocation
    keyLocation = random.choice(locations).lower()

def north():
    delayPrint("\nYou walk up to the north door. You try to open up the door but it is looked.")
    if hasattr(player, 'key'):
        delayPrint("\nYou open up the door and leave.")
        exploring = False
    else:
        delayPrint("\nYou leave the door alone.")

def south():
    delayPrint("\nYou walk in the south door. There is a polar bear the jumps on you and you die.")
    exploring = False

def east():
    delayPrint("\nYou walk to the east door. When you walk in you see an empty room")
    if playerLocation == keyLocation:
        delayPrint("\nYou found a key.")
        delayPrint("\nWould you like to pick it up?")
        getKey = False
        while getKey == False:
            playerChoice = input(prompt).lower()
            if playerChoice == "yes" or playerChoice == "y" or playerChoice =="get key":
                player.inventory = 'key'
                delayPrint("You picked up the key")
                getKey = True
            elif playerChoice == "no" or playerChoice =="n":
                delayPrint("\nOkay then. If you change your mind, just type 'Get Key'.")
            else:
                invalidInput()
    else:
        delayPrint("\nYou looked around and you found nothing.")

def west():
    delayPrint("\nYou walk to the west door.You see a skelton laying on the gound.")
    if playerLocation == keyLocation:
        delayPrint("\nYou found a key.")
        delayPrint("\nWould you like to pick it up?")
        getKey = False
        while getKey == False:
            playerChoice = input(prompt).lower()
            if playerChoice == "yes" or playerChoice == "y" or playerChoice =="get key":
                player.inventory = 'key'
                delayPrint("You picked up the key")
                getKey = True
            elif playerChoice == "no" or playerChoice =="n":
                delayPrint("\nOkay then. If you change your mind, just type 'Get Key'.")
            else:
                invalidInput()
    else:
        delayPrint("\nYou looked around and you found nothing.")

def northwest():
    delayPrint("\nYou walk to the northwest door. You find the carcass of a died dog.")
    if playerLocation == keyLocation:
        delayPrint("\nYou found a key.")
        delayPrint("\nWould you like to pick it up?")
        getKey = False
        while getKey == False:
            playerChoice = input(prompt).lower()
            if playerChoice == "yes" or playerChoice == "y" or playerChoice =="get key":
                player.inventory = 'key'
                delayPrint("You picked up the key")
                getKey = True
            elif playerChoice == "no" or playerChoice =="n":
                delayPrint("\nOkay then. If you change your mind, just type 'Get Key'.")
            else:
                invalidInput()
    else:
        delayPrint("\nYou looked around and you found nothing.")

def northeast():
    delayPrint("\nYou walk to the northwest door.You find a torture chamber.")
    if playerLocation == keyLocation:
        delayPrint("\nYou found a key.")
        delayPrint("\nWould you like to pick it up?")
        getKey = False
        while getKey == False:
            playerChoice = input(prompt).lower()
            if playerChoice == "yes" or playerChoice == "y" or playerChoice =="get key":
                player.inventory = 'key'
                delayPrint("You picked up the key")
                getKey = True
            elif playerChoice == "no" or playerChoice =="n":
                delayPrint("\nOkay then. If you change your mind, just type 'Get Key'.")
            else:
                invalidInput()
    else:
        delayPrint("\nYou looked around and you found nothing.")

# asking player for there name
delayPrint("\nWhat is your name")
player.name = input(prompt)
delayPrint("\nIt is nice to meet you " + name)
ready = False

# asking the player if they are ready
while ready == False:
    delayPrint("\nAre you ready to play?")
    choice = input(prompt)
    if choice.lower() == "yes":
        delayPrint("\nOkay we will start")
        ready = True
    elif choice.lower() == "no":
        delayPrint("\nJust tell me when you are ready")
        ready == False
    else:
        invalidInput()

newGame = True
while newGame == True:

# moves the key around randomly
    key()
##    print(keyLocation)
# begining of game
    delayPrint("\nYou have been dropped into a cave. You hear someone shouting, 'escape if you can'.")
    delayPrint("\nYou look around. You see 6 different doors. One in the north, south, east, west, northwest, and northeast.")

    exploring = True
    while exploring == True:
        delayPrint("\nWhich door do you want to go too?")
        playerChoice = input(prompt).lower()
        playerLocation = playerChoice
        if playerChoice == "northwest":
            northwest()
        elif playerChoice == "south":
            south()
        elif playerChoice == "west":
            west()
        elif playerChoice == "east":
            east()
        elif playerChoice == "northeast":
            northeast()
        elif playerChoice == "north":
            north()
        else:
            invalidInput()
    delayPrint("\n")
    delayPrint("\nWould you want to play again")
    playerResponse = input(prompt)
    if playerResponse == "yes":
        delayPrint("\nFanstastic!")
    elif playerResponse == "no":
        delayPrint("\nWhat a shame, See you next time.")
        newGame = False
    else:
        invalidInput()
        response = input(prompt).lower()
delayPrint("\nThanks for playing")