class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories_burned = 0

    def add_steps(self, steps):
        self.steps += steps
        self.calories_burned += steps // 20  # Assuming 20 steps burn 1 calorie

    def display_status(self):
        print(f"Today's Progress:")
        print(f"Steps taken: {self.steps}")
        print(f"Calories burned: {self.calories_burned}")

# Create an instance of FitnessTracker
tracker = FitnessTracker()

# Example usage of FitnessTracker 
print("Welcome to Fitness Tracker!")

while True:
    print("\nMenu:")
    print("1. Add Steps")
    print("2. Display Progress")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        steps = int(input("Enter the number of steps taken: "))
        tracker.add_steps(steps)
        print(f"{steps} steps added successfully!")

    elif choice == '2':
        tracker.display_status()

    elif choice == '3':
        print("Exiting Fitness Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 3.")  