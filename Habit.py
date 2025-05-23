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

    def check_goal_completion(self):
        # Ask user if they completed their goal
        completion_status = input(f"Did you complete your goal for '{self.name}'? (y/n): ").lower()
        return completion_status == 'y'