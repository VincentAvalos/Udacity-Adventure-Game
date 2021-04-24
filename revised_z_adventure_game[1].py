# Karate Zombie Infestation by Vincent Avalos
# This game is based mainly on ith the Knife
# , but possible to win.

import time
import os
import sys
import random


def typewriter(message, delay_1=.01, delay_2=1):  # Typewriter animation
    for char in message:
        sys.stdout.write(char)  # Prints Message
        sys.stdout.flush()  # Displays it
        if char != "\n":
            time.sleep(delay_1)  # Sleeps
        else:
            time.sleep(delay_2)

#  -----------------Intro to game-------------------


def city():
    typewriter("           K A R A T E\n")
    typewriter(" Z  O  M  B  I  E   I N F E S T A T I O N\n")
    typewriter("        b y : VA v a l o s\n")
    typewriter("""
                  ______
     _____       |      |
    |     |      |      |
    |     | _____|      | ____
    |     ||     |      ||    |    ____
    |     ||     |      ||    |  _|    |
    |     ||     |      ||  ____| |    |
    |     ||     |      || |    | |    |
    |     ||     |      |__|    | |    |
    |     ||     |      |  |    | |    |
    |     ||     |      |  |    | |    |
    |     ||     |      |  |    | |    |
    """, 0, .1)


def intro():
    story = """
It was only a few hours ago on the news that you heard about the world
wide zombie outbreak. Before going to bed you decided to lock all the
doors and block the windows that you could. Finally, you rested your
eyes and went to sleep dreaming of your Karate lessons...\n"""
    city()
    typewriter(story)
    print("\n*THONK*\n")
    wake_up = ("""
A loud sound wakes you in the middle of the
night and you spring up from your bed!
""")
    typewriter(wake_up)

# ___________________________________________


def valid_input(prompt, options):  # Input
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
            break
        typewriter(f'"{option}" isn\'t an option.\n')


# -------------To play the game again--------------


def start_game():  # Starts the game
    typewriter("Karate Zombie Infestation\n")
    typewriter("Ready to play? yes|no\n")
    answer = valid_input(">>", ['yes', 'no'])
    if "yes" in answer:
        print("\n")
        main()
    else:
        typewriter("Guess you're too scared to play...")


def Play_again():  # when 'n' break main() loop
    return valid_input("\nPlay again? y|n\n>>", ['y', 'n'])


# --Winning/Losing prompts that redirect you to the Play_again() func--


def you_won():  # Called if won
    typewriter("\nThe house has been cleared...")
    typewriter("\nBut why is everthing still dark?")


def you_died():  # Called if dead
    typewriter("\nYou died...\n")


def end_game():  # Ends the game
    typewriter("\nG A M E  O V E R\n")
    typewriter("Thanks for playing!")

#  ________________________________________


def zombie_event(weapons, zombie):  # zombie event
    zombie = random.choice([
        'one zombie!', 'two zombies!', 'nothing...',
        'a Karate Zombie Master!'
    ])
    typewriter(f"\nYou see {zombie}\n")
    global hp
    bite = random.choice(["neck", "leg", "arm", "face"])
    hp = 1
    miss = random.randint(0, 1)
    one_z = ("""
One zombie lunges at you!
You stabbed the zombie in the head!
It fell to the floor and stopped moving...
    """)
    if 'knife' in weapons:  # If you have a knife
        if zombie == 'one zombie!':  # one zombie if knife
            typewriter(one_z)
        if zombie == 'two zombies!':  # two zombie if knife
            typewriter(one_z)
            for hit in range(miss):
                hp -= 1
            if hp < 1:  # You die
                typewriter(f"""
Looks like your knife broke.
The second zombie lunges for you!
The zombie bites your {bite} \n
                """)
            else:
                typewriter(f"""
The second zombie lunges for you!
The zombie misses and falls on the floor!
You stabbed the last zombie in the head!\n
                """)  # You survive
        elif zombie == 'a Karate Zombie Master!':  # Karate master knife
            hp -= 1
            if hp < 1:
                typewriter("""
The Karate Zombie Master goes into a
Fudo-dachi stance and kicks the knife out
of your hand and does a spin-kick to
your head!\n
            """)
        elif zombie == 'nothing...':
            None
    else:  # If no knife in weapons
        if zombie == 'a Karate Zombie Master!':
            zombie_attack = random.choice(
             ["upper torso kick!", "high punch!"]
            )
            typewriter(f"""
The Karate Zombie Master goes for
a {zombie_attack} What do you do?!\n\n""")
            print("""
======Moves======
1. Counter Kick
2. Counter punch\n\n
""")
            if "upper torso kick!" in zombie_attack:
                answer = valid_input(">>", ['1', '2']).lower()
                if '1' in answer:
                    typewriter("\nYou countered his kick!\n")
                    typewriter("You defeated the Karate Zombie!")
                else:
                    hp -= 1
                    if hp < 1:  # Lose
                        typewriter("\nYou couldn't counter his kick!\n")
            if "high punch!" in zombie_attack:
                answer = valid_input(">>", ['1', '2']).lower()
                if '1' in answer:
                    hp -= 1
                    if hp < 1:
                        typewriter("\nYou couldn't counter his punch!\n")
                else:
                    typewriter("\nYou countered his punch!")
                    typewriter("You defeated the Karate Zombie!")
        elif zombie == 'nothing':
            None
        else:
            karate(zombie)


def karate(zombie):  # Called if no weapon
    attacks = random.choice([
        'Gedan Tuski punch', 'Chudan Tuski punch',
        'Kikomi Geri kick', 'Ushiro Geri kick',
        'Masui kick'
    ])
    if zombie == 'two zombies!':
        typewriter(f"""
You attack one zombie with a {attacks}""")
        attacks = random.choice([
             'Gedan Tuski punch', 'Chudan Tuski punch',
             'Kikomi Geri kick', 'Ushiro Geri kick',
             'Masui kick'
        ])
        typewriter(f"""
and the other zombie with a {attacks}!
The zombies died on impact!
        """)
    elif zombie == 'one zombie!':
        typewriter(f"""
You used a {attacks} on the zombie!
The zombie died on impact!
        """)


# ----------------------Lights----------------------


def light_on(lights, which_light):
    typewriter("\n\nIt's too dark to see anything.")
    typewriter(" You should turn the light on. 'ON'")
    answer = valid_input("\n>>", "on").lower()
    if "on" in answer:
        lights.append(which_light)
        print("\n*FLick*\n")
        typewriter(f"You turn the {which_light} on.")
    else:
        light_on(lights, which_light)


# ----------------------------The Cake of the game------------------------


def bedroom(weapons, lights, zombie):
    if "bedroom light" in lights:
        typewriter("\n\nYou see a knife. Do you want to pick up the knife?")
        typewriter(" yes|no\n")
        answer = valid_input(">>", ['yes', 'no']).lower()
        if 'yes' in answer:
            typewriter("\nYou picked up the knife. It's kind of dull...\n\n")
            weapons.append("knife")
            typewriter("You grab the door knob to the hallway and enter.\n")
            hallway(weapons, lights, zombie)
        else:
            typewriter("\nFear invades your brain...\n\n")
            typewriter("You grab the door knob to the hallway and enter.\n")
            hallway(weapons, lights, zombie)
    else:
        light_on(lights, "bedroom light")
        bedroom(weapons, lights, zombie)


def hallway(weapons, lights, zombie):
    if "hallway light" in lights:
        zombie_event(weapons, zombie)
        if hp > 0:
            typewriter("\nYou make your way into the living room...")
            living_room(weapons, lights, zombie)
        else:
            you_died()
    else:
        light_on(lights, "hallway light")
        hallway(weapons, lights, zombie)


def living_room(weapons, lights, zombie):
    if "living room light" in lights:
        zombie_event(weapons, zombie)
        if hp > 0:
            you_won()
        else:
            you_died()
    else:
        light_on(lights, "living room light")
        living_room(weapons, lights, zombie)


# -------------------The game loop and scopes----------------


def main():
    while True:
        lights = []
        weapons = []
        zombie = random.choice([
            'one zombie!', 'two zombies!',
            'nothing...', 'a Karate Zombie Master!'
        ])
        intro()
        bedroom(weapons, lights, zombie)
        if Play_again() == 'n':
            break
    end_game()


if __name__ == '__main__':
    start_game()
