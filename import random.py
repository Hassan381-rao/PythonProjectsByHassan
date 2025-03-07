import random

# Constants for dice faces
ONE = "⚀"
TWO = "⚁"
THREE = "⚂"
FOUR = "⚃"
FIVE = "⚄"
SIX = "⚅"

def roll_dice():
    # Simulate rolling a six-sided die
    rolled_number = random.randint(1, 6)
    
    # Display the result
    print(f"Rolled: {rolled_number} ({[ONE, TWO, THREE, FOUR, FIVE, SIX][rolled_number - 1]})")

if __name__ == "__main__":
    roll_dice()
