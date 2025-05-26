# Import required datetime modules for date handling
from datetime import datetime, timedelta

# Define a class to manage and track user habits
class Habit:
    def __init__(self, name, habit_type, goal, start_date, end_date):
        # Store basic habit information
        self.name = name            # Name of the habit
        self.habit_type = habit_type # Type of habit (e.g., daily, weekly)
        self.goal = goal            # The target goal for this habit
        
        # Convert string dates to datetime objects and perform validation
        try:
            # Convert start date string to datetime object
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            # Convert end date string to datetime object
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            
            # Make sure end date comes after start date
            if self.end_date <= self.start_date:
                raise ValueError("End date must be after start date")
                
        except ValueError as e:
            # If any date conversion or validation fails, raise an error
            raise ValueError(f"Date error: {str(e)}")
            
        # Initialize tracking variables
        self.streak = 0                # Current streak counter
        self.last_completion = None    # Last time habit was completed
        self.completed_today = False   # Flag for today's completion status
        self.completion_history = {}   # Dictionary to store completion dates and times

    def check_goal_completion(self):
        # Get current date and time
        current_time = datetime.now()
        current_date = current_time.date()

        # Check if habit tracking period has started
        if current_date < self.start_date:
            print("This habit hasn't started yet!")
            return False
            
        # Check if habit tracking period has ended
        if current_date > self.end_date:
            print("This habit has ended!")
            return False

        # Check if habit is already completed for today
        if current_date.strftime("%Y-%m-%d") in self.completion_history:
            print("You've already completed this habit today!")
            return False

        # Ask user for habit completion status
        completion_status = input(f"Did you complete your goal for '{self.name}'? (y/n): ").lower()
        
        # If user completed the habit
        if completion_status == 'y':
            # Update completion tracking information
            self.last_completion = current_time
            self.completion_history[current_date.strftime("%Y-%m-%d")] = current_time
            self.completed_today = True
            return True
        return False

    def calculate_streak(self):
        # Return 0 if no completions recorded
        if not self.completion_history:
            return 0
        
        # Get current date for streak calculation
        current_date = datetime.now().date()
        streak = 0
        check_date = current_date

        # Count consecutive days of completion
        while check_date.strftime("%Y-%m-%d") in self.completion_history:
            streak += 1
            check_date -= timedelta(days=1)
            
        return streak