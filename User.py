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
    
    def update_app_locks(self, completed):
        # Update app locks based on habit completion and selected mode
        if self.mode == "reward":
            # In reward mode, unlock an app when user completes a goal
            if completed:
                if self.locked_apps:
                    app_to_unlock = self.locked_apps.pop(0)
                    print(f"{Fore.GREEN}App unlocked: {app_to_unlock}{Style.RESET_ALL}")
        elif self.mode == "punishment":
            # In punishment mode, lock an app when user fails a goal
            if not completed and self.favorite_apps:
                # Lock a random app
                if len(self.locked_apps) < len(self.favorite_apps):
                    unlocked_apps = [app for app in self.favorite_apps if app not in self.locked_apps]
                    app_to_lock = random.choice(unlocked_apps)
                    self.locked_apps.append(app_to_lock)
                    print(f"{Fore.RED}App locked: {app_to_lock}{Style.RESET_ALL}")