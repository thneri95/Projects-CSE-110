"""
Author: Tiago Borges
W03 Project Final: Adventure Game
Title: The Mysterious Forest


Description: 
This is a text-based adventure game with three levels of choices
Creativity: For the final version, I added random events using 
the random module and some hidden options to make the game more dynamic and engaging.
"""

import random

# Game Introduction
print("You are standing at the edge of a mysterious forest. Do you ENTER the forest or TURN BACK?")
choice = input("Type your choice (ENTER or TURN BACK): ").strip().lower()

if choice == "enter":
    print("You bravely step into the forest, and the trees close behind you. In the distance, you hear a strange sound.")
    print("Do you MOVE TOWARDS the sound or EXPLORE another path?")
    choice = input("Type your choice (MOVE TOWARDS or EXPLORE): ").strip().lower()

    if choice == "move towards":
        # Random Event 1: Encounter a Wild Animal
        event = random.choice(["bear", "wolf", "nothing"])
        if event == "bear":
            print("You encounter a grizzly bear! You must RUN or HIDE.")
            choice = input("Type your choice (RUN or HIDE): ").strip().lower()
            if choice == "run":
                print("You run as fast as you can and escape the bear. That was close!")
            elif choice == "hide":
                print("You hide behind a tree, and the bear eventually leaves. You survive!")
            else:
                print("Invalid choice. The bear notices you, and you are forced to retreat.")
        elif event == "wolf":
            print("You encounter a wolf pack! You run away to safety.")
        else:
            print("You hear rustling in the bushes, but it's just the wind. You move on safely.")

        # Continuing the scenario
        print("You approach a hooded figure. They offer you a choice: take a MAP or a COMPASS.")
        choice = input("Type your choice (MAP or COMPASS): ").strip().lower()

        if choice == "map":
            print("The map leads you to hidden treasure! You win!")
        elif choice == "compass":
            print("The compass guides you safely out of the forest. You survive!")
        else:
            print("Invalid choice. The figure disappears, and you are lost in the forest.")

    elif choice == "explore":
        # Random Event 2: Fall into a Trap
        event = random.choice(["trap", "hidden_path", "nothing"])
        if event == "trap":
            print("You fall into a hidden trap! You struggle to get out and lose valuable time.")
        elif event == "hidden_path":
            print("You discover a hidden path that leads to a mysterious cave.")
        else:
            print("You wander for a while, but find nothing unusual.")

        # Continuing the scenario
        print("You find a cave with a treasure chest. Do you LOOK FOR a KEY or try to FORCE it open?")
        choice = input("Type your choice (KEY or FORCE): ").strip().lower()

        if choice == "key":
            print("You find a key and open the chest, revealing gold and jewels. You win!")
        elif choice == "force":
            print("The chest is trapped! It explodes, and you lose the game.")
        else:
            print("Invalid choice. The cave collapses, and you are trapped inside.")

    else:
        print("Invalid choice. You wander aimlessly in the forest.")

elif choice == "turn back":
    # Random Event 3: Unexpected Encounter
    event = random.choice(["nothing", "traveler"])
    if event == "traveler":
        print("On your way back, you meet a wise traveler who shares stories about the forest.")
    else:
        print("You decide not to enter the forest and return home safely, missing out on a great adventure.")

else:
    print("Invalid choice. Please restart the game and choose ENTER or TURN BACK.")

print("\nEnd of the game. Thank you for playing!")


# This project was quite challenging but it taught me a lot about Python and problem-solving
# I faced some difficulties with syntax and logic, but after troubleshooting, I was able to make it work
# Adding random events and multiple scenarios made the game more engaging and dynamic
# Thank you for taking the time to review my work!

 
