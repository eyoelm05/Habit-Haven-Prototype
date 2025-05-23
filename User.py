from colorama import init, Fore, Style  # Import colorama for colored terminal output - 
#install with `pip install colorama`
import random  # For random app selection
init()  # Initialise colorama

class User:
    def __init__(self, username, password):
        # Initialize user with their basic info and empty collections
        self.username = username
        self._password = password
        self.habits = []  # List to store user's habits
        self.favorite_apps = []  # Store user's favorite apps that can be locked/unlocked
        self.locked_apps = []  # Track which apps are currently locked
        self.completed_goals = 0  # Counter for completed goals
        self.mode = None  # Track user's preference: "reward" or "punishment"

    def add_habit(self, habit):
        # Add habit to habits list
        self.habits.append(habit)
        return True

    def add_favorite_app(self, app_name):
        # Add app to favorites (max 3 apps)
        if len(self.favorite_apps) < 3:
            self.favorite_apps.append(app_name)
            return True
        return False