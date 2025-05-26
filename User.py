# Import required modules for colors, random selection, and date/time operations
from colorama import init, Fore, Style
import random
from datetime import datetime, timedelta

# Initialize colorama for colored terminal output
init()

# Main User class definition
class User:
    # Constructor method to create a new user
    def __init__(self, username, password):
        self.username = username  # Store the username
        self._password = password  # Store the password (protected variable)
        self.habits = []  # List to store user's habits
        self.favorite_apps = []  # List to store user's favorite apps
        self.locked_apps = {}  # Dictionary to store locked apps and their lock timestamps
        self.completed_goals = 0  # Counter for completed goals
        self.mode = None  # User's mode (reward/punishment)
        self.last_reset = datetime.now().date()  # Track last reset date

    # Method to add a new habit to user's habit list
    def add_habit(self, habit):
        self.habits.append(habit)  # Add the habit to the list
        return True

    # Method to add a favorite app (maximum 3 allowed)
    def add_favorite_app(self, app_name):
        if len(self.favorite_apps) < 3:  # Check if under the limit
            self.favorite_apps.append(app_name)  # Add the app
            return True
        return False  # Return False if limit reached

    # Method to check and perform daily reset operations
    def check_daily_reset(self):
        current_date = datetime.now().date()  # Get current date
        if current_date > self.last_reset:  # Check if day has changed
            # Reset completion status for all habits
            for habit in self.habits:
                habit.completed_today = False
            
            # If in reward mode, lock all apps at midnight
            if self.mode == "reward":
                self.locked_apps = {app: self.locked_apps.get(app, datetime.now()) 
                                  for app in self.favorite_apps}
            self.last_reset = current_date  # Update last reset date

    # Method to update app locks based on habit completion
    def update_app_locks(self, completed):
        """Update app locks based on habit completion"""
        current_time = datetime.now()
        
        if self.mode == "reward":
            if completed:
                # Get all locked apps
                locked_apps = list(self.locked_apps.keys())
                if locked_apps:
                    # Randomly select an app to unlock
                    app_to_unlock = random.choice(locked_apps)
                    lock_time = self.locked_apps[app_to_unlock]
                    lock_duration = current_time - lock_time
                    
                    # Remove the app from locked_apps
                    del self.locked_apps[app_to_unlock]
                    
                    # Print unlock message with duration
                    print(f"{Fore.GREEN}🎉 App unlocked: {app_to_unlock}")
                    print(f"Was locked for: {lock_duration.days} days, "
                          f"{lock_duration.seconds//3600} hours{Style.RESET_ALL}")
        
        elif self.mode == "punishment":
            if not completed:
                # Get all unlocked apps
                unlocked_apps = [app for app in self.favorite_apps 
                               if app not in self.locked_apps]
                if unlocked_apps:
                    # Randomly select an app to lock
                    app_to_lock = random.choice(unlocked_apps)
                    self.locked_apps[app_to_lock] = current_time
                    print(f"{Fore.RED}🔒 App locked: {app_to_lock}{Style.RESET_ALL}")

    # Method to set the user mode (reward or punishment)
    def set_mode(self, mode):
        """Set user mode and initialize app locks accordingly"""
        self.mode = mode
        if mode == "reward":
            # Lock all apps initially
            self.locked_apps = {app: datetime.now() for app in self.favorite_apps}
        else:
            # For punishment mode, start with all apps unlocked
            self.locked_apps = {}