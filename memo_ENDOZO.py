
import os

# Importing activities
from activity1 import act1
from activity2 import act2
from activity3 import act3
from activity4 import act4
from activity5 import act5
from activity6 import act6
from activity7 import act7
from activity8 import act8
from activity9 import act9
from activity10 import act10
from activity11 import act11
from activity12 import act12
from activity13 import act13
from activity14 import act14
from activity15 import act15
from activity16 import act16
from activity17 import act17
from activity18 import act18
from activity19 import act19
from activity20 import act20
from activity21 import act21
from activity23 import act23
from activity24 import act24
from activity25 import act25

# Importing code challenges
from code_challenge1 import cc1
from code_challenge2 import cc2
from code_challenge3 import cc3
from code_challenge4 import cc4
from code_challenge5 import cc5
from code_challenge6 import cc6
from code_challenge7 import cc7
from code_challenge8 import cc8
from code_challenge9 import cc9
from code_challenge10 import cc10
from code_challenge11 import cc11
from code_challenge12 import cc12
from code_challenge13 import cc13
from code_challenge14 import cc14
from code_challenge15 import cc15

# Function to clear the screen (cross-platform)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function
def finals():
    # Activity and Code Challenge Mappings
    activities = {
        "1": act1, "2": act2, "3": act3, "4": act4, "5": act5,
        "6": act6, "7": act7, "8": act8, "9": act9, "10": act10,
        "11": act11, "12": act12, "13": act13, "14": act14, "15": act15,
        "16": act16, "17": act17, "18": act18, "19": act19, "20": act20,
        "21": act21, "23": act23, "24": act24, "25": act25
    }

    code_challenges = {
        "1": cc1, "2": cc2, "3": cc3, "4": cc4, "5": cc5,
        "6": cc6, "7": cc7, "8": cc8, "9": cc9, "10": cc10,
        "11": cc11, "12": cc12, "13": cc13, "14": cc14, "15": cc15
    }

    # Program Start
    name = input("Please enter your name: ")

    while True:
        clear_screen()
        print(f"Hello, {name}.")
        print("\n====== Main Menu ======")
        print("1. Activities")
        print("2. Code Challenges")
        print("3. Exit")

        choice = input("Choose a number: ")

        if choice == "1":
            while True:
                activity_choice = input("Choose an activity (1-25, 0 to exit): ")
                if activity_choice == "0":
                    break
                elif activity_choice in activities:
                    clear_screen()
                    print(f"Executing Activity {activity_choice}...\n")
                    activities[activity_choice]()
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "2":
            while True:
                challenge_choice = input("Choose a code challenge (1-15, 0 to exit): ")
                if challenge_choice == "0":
                    break
                elif challenge_choice in code_challenges:
                    clear_screen()
                    print(f"Executing Code Challenge {challenge_choice}...\n")
                    code_challenges[challenge_choice]()
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Program terminated. Goodbye!")
            break

        else:
            print("Invalid number. Please try again.")

# Start the program
finals()