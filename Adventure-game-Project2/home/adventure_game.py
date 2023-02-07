

import time
import random


def pause():
    time.sleep(2)


choosePath = ["1", "2"]
path = ""

animal = [" bear ", " lion ", " cheetah ", " wolf "]
random.choice(animal)


def lost():
    pause()
    print("You waking Up in the middle of the night ")
    pause()
    print("You found yourself lost in dark forest ")
    pause()
    print("You are ALONE, you are TERRIFIED")
    pause()
    print("You can only hear noises around you")
    pause()
    print("You find berries in a little tree")
    pause()
    print("Enter 1 to Eat berries")
    print("Enter 2 to Search more")


lost()
while path not in choosePath:
    path = str(input("Choose Path? (1 or 2): "))


def choose1():
    print("You decide to eat the berries because you are starving ")
    pause()
    print("due to eating poisonous berries, you feel lightheaded ")
    pause()
    print("YOU DEAD ")
    print("Game over")
    playchoose = ["Yes", "No"]
    play = str(input("Play again?[Yes / No]: "))
    while play not in playchoose:
        play = str(input("Play again?[Yes / No]: "))
    if play == "Yes":
        print("...")
        lost()
        choosePath = ["1", "2"]
        path = ""
        while path not in choosePath:
            path = str(input("Choose Path? (1 or 2): "))
        if path == choosePath[0]:
            choose1()
        elif path == choosePath[1]:
            choose2()
    elif play == "No":
        print("Thank you for playing,hope you enjoyed.")


def choose2():
    wildanimal = random.choice(animal)
    print("You decide to look for something that might be helpful ")
    pause()
    print("while you are walking you notice")
    pause()
    print("something moving between the trees")
    pause()
    print("Then the" + wildanimal + "appear")
    pause()
    print("You shock")
    pause()
    print("And the first thing come to your mind is RUN!!")
    pause()
    print("You run faster and faster as you can")
    pause()
    print("You are faced with two unknown paths")
    way = str(input("Do you want to go right or left?"))
    RorL = ["right", "left"]
    while way not in RorL:
        way = str(input("Do you want to go right or left?"))
    if way == "right":
        right(wildanimal)
    elif way == "left":
        left(wildanimal)


def complet(wildanimal):
    print("You can escape and the" + wildanimal + "disappear")
    pause()
    print("After a moment, you notice a village")
    pause()
    print("The villagers was nice and friendly they welcome you")
    pause()
    print("You become villager! congrats you win the game!")
    playchoose = ["Yes", "No"]
    play = str(input(" Play again?[Yes / No]: "))
    while play not in playchoose:
        play = str(input("Play again?[Yes / No]: "))
    if play == "Yes":
        print("...")
        lost()
        choosePath = ["1", "2"]
        path = ""
        while path not in choosePath:
            path = str(input("Choose Path? (1 or 2): "))
        if path == choosePath[0]:
            choose1()
        elif path == choosePath[1]:
            choose2()
    elif play == "No":
        print("Thank you for playing,hope you enjoyed.")


def right(wildanimal):
    print("Because The " + wildanimal + " is old he was slow")
    pause()
    complet(wildanimal)


def left(wildanimal):
    print("Wrong decision it's Dead End Path")
    pause()
    print(wildanimal + "attack you")
    pause()
    print("Game over")
    playchoose = ["Yes", "No"]
    play = str(input(" Play again?[Yes / No]: "))
    while play not in playchoose:
        play = str(input("Play again?[Yes / No]: "))
    if play == "Yes":
        print("...")
        lost()
        choosePath = ["1", "2"]
        path = ""
        while path not in choosePath:
            path = str(input("Choose Path? (1 or 2): "))
        if path == choosePath[0]:
            choose1()
        elif path == choosePath[1]:
            choose2()
    elif play == "No":
        print("Thank you for playing,hope you enjoyed.")


if path == choosePath[0]:
    choose1()
elif path == choosePath[1]:
    choose2()