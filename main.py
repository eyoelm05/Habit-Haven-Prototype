from colorama import init, Fore, Style  # Import colorama for colored terminal output - 
#install with `pip install colorama`
from datetime import datetime, timedelta  # For date handling
from User import User
from Habit import Habit
import random  # For random app selection
init()  # Initialise colorama

def main():
        # Main application entry point
        # Get user credentials
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = User(username, password)
        print(f"Hello, {user.username}! You're logged in.")
        
        # First add just 1 habit
        print("\nLet's start by adding a habit to track:")

        # Ask if user wants to add more habits
        while True:
            habit = createHabit()
            user.habits.append(habit)

            add_more = input("\nDo you want to add another habit? (y/n): ").lower()
            if add_more != 'y':
                break


def createHabit():
    while True:
        # Helper method to add a new habit
        habit_type = input("Do you want to build or break a habit? (build/break): ").lower()

        if habit_type == "build":
            # Add a habit to build (something new to develop)
            habit_name = input("Enter the habit you want to build: ")
            start_date = input("Start date (YYYY-MM-DD) or press Enter for today: ")
            if not start_date:
                start_date = datetime.today().strftime("%Y-%m-%d")
            end_date = input("Tentative end date (YYYY-MM-DD): ")
            
            new_habit = Habit(habit_name, "build", "", start_date, end_date)
            print(f"Great! You've started tracking: {habit_name}")
            return new_habit
        
        elif habit_type == "break":
            # Add a habit to break (something to stop doing)
            habit_name = input("Enter the habit you want to break: ")
            start_date = input("Start date (YYYY-MM-DD) or press Enter for today: ")
            if not start_date:
                start_date = datetime.today().strftime("%Y-%m-%d")
            end_date = input("Tentative end date (YYYY-MM-DD): ")
            
            new_habit = Habit(habit_name, "break", "", start_date, end_date)
            print(f"Great! You'll work on breaking: {habit_name}")
            return new_habit
        else:
            # Handle invalid input
            print("Invalid choice. Please choose 'build' or 'break'.")


if __name__ == "__main__":
        main()