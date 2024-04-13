import random

def roll_dice(num_sides, num_rolls):
    print(f"Rolling {num_rolls} dice with {num_sides} sides:")
    for i in range(num_rolls):
        roll_result = random.randint(1, num_sides)
        print(f"Roll {i+1}: {roll_result}")

def dice_rolling_simulator():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice: "))
            if num_sides <= 0:
                raise ValueError("Number of sides must be greater than zero.")
            break
        except ValueError as e:
            print("Invalid input. Please enter a positive integer for the number of sides.")

    while True:
        try:
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls <= 0:
                raise ValueError("Number of rolls must be greater than zero.")
            break
        except ValueError as e:
            print("Invalid input. Please enter a positive integer for the number of rolls.")

    roll_dice(num_sides, num_rolls)

    play_again = input("Do you want to roll again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for rolling the dice!")
    else:
        dice_rolling_simulator()

dice_rolling_simulator()
