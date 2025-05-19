from colorama import init, Fore, Style  # Import colorama for colored terminal output - 
#install with `pip install colorama`
from datetime import datetime, timedelta  # For date handling
import random  # For random app selection
import time  # For time-related functions
init()  # Initialise colorama

class User:
    def __init__(self, email, password):
        # Initialize user with their basic info and empty collections
        self.email = email
        self.password = password
        self.habits = []  # List to store user's habits
        self.favorite_apps = []  # Store user's favorite apps that can be locked/unlocked
        self.locked_apps = []  # Track which apps are currently locked
        self.completed_goals = 0  # Counter for completed goals
        self.mode = None  # Track user's preference: "reward" or "punishment"
        
    def add_favorite_app(self, app_name):
        # Add app to favorites (max 3 apps)
        if len(self.favorite_apps) < 3:
            self.favorite_apps.append(app_name)
            return True
        return False
        
    def check_goal_completion(self, habit):
        # Ask user if they completed their goal
        completion_status = input(f"Did you complete your goal for '{habit.name}'? (y/n): ").lower()
        return completion_status == 'y'
    
    def update_app_locks(self, habit_completed):
        # Update app locks based on habit completion and selected mode
        if self.mode == "reward":
            # In reward mode, unlock an app when user completes a goal
            if habit_completed:
                if self.locked_apps:
                    app_to_unlock = self.locked_apps.pop(0)
                    print(f"{Fore.GREEN}App unlocked: {app_to_unlock}{Style.RESET_ALL}")
        elif self.mode == "punishment":
            # In punishment mode, lock an app when user fails a goal
            if not habit_completed and self.favorite_apps:
                # Lock a random app
                if len(self.locked_apps) < len(self.favorite_apps):
                    unlocked_apps = [app for app in self.favorite_apps if app not in self.locked_apps]
                    app_to_lock = random.choice(unlocked_apps)
                    self.locked_apps.append(app_to_lock)
                    print(f"{Fore.RED}App locked: {app_to_lock}{Style.RESET_ALL}")

class Habit:
    def __init__(self, name, habit_type, goal, start_date, end_date):
        # Initialise a habit with its properties
        self.name = name
        self.habit_type = habit_type  # "build" or "break"
        self.goal = goal  # Description of target/goal
        self.start_date = start_date
        self.end_date = end_date
        self.streak = 0  # Track consecutive days of completion
        self.last_checked = None  # Store when habit was last checked

class AuthApp:
    def __init__(self):
        # Initialise app with motivational messages
        self.motivational_messages = [
            "You're doing great! Keep it up!",
            "Every small step counts toward big progress!",
            "Stay focused, you're on the right track!",
            "Your future self will thank you for your commitment today!",
            "Consistency is the key to building lasting habits!"
        ]
    
    def run(self):
        # Main application entry point
        # Get user credentials
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = User(email, password)
        print(f"Hello, {user.email}! You're logged in.")
        
        # First add just 1 habit
        print("\nLet's start by adding a habit to track:")
        self.add_habit(user)
        
        # Ask if user wants to add more habits
        while True:
            add_more = input("\nDo you want to add another habit? (y/n): ").lower()
            if add_more != 'y':
                break
            self.add_habit(user)
            
        # Setup favorite apps for locking/unlocking
        print("\nNow, let's set up your 3 favorite apps that will be subject to locking/unlocking:")
        for i in range(3):
            app_name = input(f"Enter favorite app #{i+1}: ")
            user.add_favorite_app(app_name)
        
        # Choose enforcement mode (reward or punishment)
        print("\nChoose your habit enforcement mode:")
        print("1. Reward Mode - Apps start locked and get unlocked as you complete tasks")
        print("2. Punishment Mode - Apps start unlocked but get locked if you fail tasks")
        mode_choice = input("Choose mode (1/2): ")
        
        if mode_choice == "1":
            # Set up reward mode - all apps start locked
            user.mode = "reward"
            user.locked_apps = user.favorite_apps.copy()
            print(f"{Fore.YELLOW}All apps are locked. Complete tasks to unlock them!{Style.RESET_ALL}")
        else:
            # Set up punishment mode - all apps start unlocked
            user.mode = "punishment"
            print(f"{Fore.GREEN}All apps are unlocked. Don't fail tasks or they'll get locked!{Style.RESET_ALL}")
        
        # Start the main application menu
        self.habit_menu(user)
    
    def add_habit(self, user):
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
            user.habits.append(new_habit)
            print(f"Great! You've started tracking: {habit_name}")
            
        elif habit_type == "break":
            # Add a habit to break (something to stop doing)
            habit_name = input("Enter the habit you want to break: ")
            start_date = input("Start date (YYYY-MM-DD) or press Enter for today: ")
            if not start_date:
                start_date = datetime.today().strftime("%Y-%m-%d")
            end_date = input("Tentative end date (YYYY-MM-DD): ")
            
            new_habit = Habit(habit_name, "break", "", start_date, end_date)
            user.habits.append(new_habit)
            print(f"Great! You'll work on breaking: {habit_name}")
        
        else:
            # Handle invalid input
            print("Invalid choice. Please choose 'build' or 'break'.")
            return self.add_habit(user)
    
    def display_motivational_message(self):
        # Show a random motivational message
        message = random.choice(self.motivational_messages)
        print(f"\n{Fore.YELLOW}💪 {message}{Style.RESET_ALL}")
    
    def habit_menu(self, user):
        # Main application menu
        while True:
            # Display menu options
            print("\n1. Add another habit")
            print("2. View habits")
            print("3. Check goal completion")
            print("4. View app status")
            print("5. Get motivation")
            print("6. Exit")
            
            choice = input("Choose an option (1-6): ")
            
            if choice == "1":
                # Add a new habit
                self.add_habit(user)
                
            elif choice == "2":
                # View all tracked habits
                if not user.habits:
                    print("\nNo habits tracked yet!")
                else:
                    print("\nYour Habits:")
                    for habit in user.habits:
                        color = Fore.MAGENTA if habit.habit_type == "build" else Fore.CYAN
                        print(f"{color}{habit.name} - {habit.habit_type.upper()}{Style.RESET_ALL}")
                        if habit.goal:  # Only show goal if it exists
                            print(f"  Goal: {habit.goal}")
                        print(f"  Period: {habit.start_date} to {habit.end_date}")
                        print(f"  Current streak: {habit.streak} days")
            
            elif choice == "3":
                # Check if a habit's goal was completed
                if not user.habits:
                    print("\nNo habits tracked yet!")
                else:
                    # Show list of habits to check
                    print("\nCheck Goal Completion:")
                    for i, habit in enumerate(user.habits):
                        print(f"{i+1}. {habit.name}")
                    
                    # Ask which habit to check
                    habit_idx = int(input("Select habit to check (number): ")) - 1
                    if 0 <= habit_idx < len(user.habits):
                        habit = user.habits[habit_idx]
                        completed = user.check_goal_completion(habit)
                        
                        if completed:
                            # Handle successful completion
                            habit.streak += 1
                            user.completed_goals += 1
                            print(f"{Fore.GREEN}Great job! Your streak is now {habit.streak} days.{Style.RESET_ALL}")
                        else:
                            # Handle failure
                            if habit.streak > 0:
                                habit.streak = 0
                                print(f"{Fore.RED}Streak reset to 0. You can do better tomorrow!{Style.RESET_ALL}")
                            else:
                                print(f"{Fore.RED}Keep trying! Tomorrow is a new day.{Style.RESET_ALL}")
                        
                        # Update app locks based on completion
                        user.update_app_locks(completed)
                        
                        # Show reminder for next check
                        next_check = datetime.now() + timedelta(days=1)
                        print(f"\n⏰ Reminder: Next check scheduled for {next_check.strftime('%A, %B %d')}")
                        
                        # Show a motivational message
                        self.display_motivational_message()
                    else:
                        print("Invalid selection.")
            
            elif choice == "4":
                # View app status (locked/unlocked)
                print(f"\nYou've completed {user.completed_goals} goals so far!")
                print(f"\nApp Status ({user.mode.capitalize()} Mode):")
                
                for app in user.favorite_apps:
                    if app in user.locked_apps:
                        print(f"  {Fore.RED}🔒 {app} (LOCKED){Style.RESET_ALL}")
                    else:
                        print(f"  {Fore.GREEN}🔓 {app} (UNLOCKED){Style.RESET_ALL}")
            
            elif choice == "5":
                # Display a motivational message
                self.display_motivational_message()
            
            elif choice == "6":
                # Exit the application
                print("Goodbye!")
                break
            else:
                # Handle invalid menu selection
                print("Invalid choice. Please try again.")

# Main entry point - start the application
if __name__ == "__main__":
    AuthApp().run()