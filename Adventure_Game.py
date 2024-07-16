import random
import time


ENEMY = ["scary dragon", "wicked fairy", "gorgon"]
weapons = []
chosen_enemy = []


def print_pause(text):
    print(text)
    time.sleep(1.5)


def intro(chosen_enemy):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + chosen_enemy + " is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


def house_or_cave():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        enter_hs_or_cv = input("Please enter 1 or 2.")
        if enter_hs_or_cv == "1":
            house()
            break
        elif enter_hs_or_cv == "2":
            cave()
            break


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a " + chosen_enemy + ".")
    print_pause("Eep! This is the " + chosen_enemy + "'s house!")
    print_pause("The " + chosen_enemy + " attacks you!")
    fight()


def cave():
    if "sword" in weapons:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten "
                    "all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        house_or_cave()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You walk back out to the field.\n")
        weapons.append("sword")
        house_or_cave()


def fight():
    if "sword" in weapons:
        while True:
            fight_or_run_sword = input("Would you like to (1) fight "
                                       "or (2) run away?:\n")
            if fight_or_run_sword == "1":
                print_pause("As the " + chosen_enemy + " moves to attack,"
                            " you unsheath your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in your "
                            "hand as you brace yourself for the attack.")
                print_pause("But the " + chosen_enemy + " takes one look "
                            "at your shiny new toy and runs away!")
                print_pause("You have rid the town of the " + chosen_enemy +
                            ". You are victorious!")
                time.sleep(2)
                play_again()
                break
            elif fight_or_run_sword == "2":
                print_pause("You run back into the field. "
                            "Luckily, you don't seem to have been followed.")
                time.sleep(2)
                house_or_cave()
                break
    else:
        print_pause("You feel a bit under-prepared for this,"
                    "with only having a tiny dagger.")
        while True:
            fight_or_run = input("Would you like to (1) "
                                 "fight or (2) run away?:\n")
            if fight_or_run == "1":
                print_pause("You do your best...")
                print_pause("But your dagger is no "
                            "match for the " + chosen_enemy + ".")
                print_pause("You have been defeated!")
                play_again()
                break
            elif fight_or_run == "2":
                print_pause("You run back into the field."
                            "Luckily, you don't seem to have been followed.\n")
                house_or_cave()
                break


def play_again():
    while True:
        play_again_prompt = input("Would you like to play again? (y/n):\n")
        if play_again_prompt == "y":
            print_pause("Excellent! Restarting the game...")
            start_game()
            break
        if play_again_prompt == "n":
            print_pause("Thanks for playing! See you next time.")
            exit()


def start_game():
    global chosen_enemy
    chosen_enemy = random.choice(ENEMY)
    intro(chosen_enemy)
    house_or_cave()
    fight()


start_game()
