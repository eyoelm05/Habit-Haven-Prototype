from datetime import datetime, timedelta
from Habit import Habit
from User import User
from Motivation import Motivation
from colorama import init, Fore, Style

init()

# Function to create and return a new habit
def createHabit():
    # Start an infinite loop for habit type input
    while True:
        # Ask user if they want to build or break a habit and convert to lowercase
        habit_type = input("Do you want to build or break a habit? (build/break): ").lower()
        
        # Check if user entered either 'build' or 'break'
        if habit_type in ["build", "break"]:
            # Get habit name and ensure it's not empty
            while True:
                habit_name = input("Enter the habit: ").strip()
                if habit_name:
                    break
                print("Habit name cannot be empty. Please enter a valid habit.")
                
            # Start an infinite loop for date input
            while True:
                try:
                    # Get start date from user; if empty, use today's date
                    start_date_input = input("Start date (YYYY-MM-DD) or press Enter for today: ").strip()
                    if not start_date_input:
                        # Convert today's date to string format YYYY-MM-DD
                        start_date = datetime.today().strftime("%Y-%m-%d")
                    else:
                        start_date = start_date_input
                    # Validate start date format
                    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
                    
                    # Get end date from user; if empty, use default (30 days later)
                    end_date_input = input("Tentative end date (YYYY-MM-DD) or press Enter for default (30 days later): ").strip()
                    if not end_date_input:
                        default_end_date = start_date_obj + timedelta(days=30)
                        end_date = default_end_date.strftime("%Y-%m-%d")
                    else:
                        end_date = end_date_input
                    # Validate end date format
                    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
                    
                    # Ensure end date is after start date
                    if end_date_obj.date() <= start_date_obj.date():
                        print("End date must be after start date!")
                        continue

                    # Create new Habit object with the collected information
                    new_habit = Habit(habit_name, habit_type, "", start_date, end_date)
                    
                    if habit_type == "build":
                        print(f"Great! You've started tracking: {habit_name}")
                    else:
                        print(f"Great! You'll work on breaking: {habit_name}")
                    # Return the created habit
                    return new_habit

                # Handle any errors in date parsing
                except ValueError as e:
                    # Show error message and continue loop
                    print(f"Error: {str(e)}")
        else:
            # Show error for invalid habit type
            print("Invalid choice. Please choose 'build' or 'break'.")

# Call the createHabit function to execute the habit creation process
def login():
    """Get username and password from user"""
    # Ask user for their username with cyan colored text
    username = input(f"{Fore.CYAN}Enter your username: {Style.RESET_ALL}")
    # Ask user for their password with cyan colored text
    password = input(f"{Fore.CYAN}Enter your password: {Style.RESET_ALL}")
    # Display welcome message in green
    print(f"\n{Fore.GREEN}Hello, {username}! You're logged in.{Style.RESET_ALL}\n")
    # Create and return a new User object
    return User(username, password)

def setup_apps(user):
    """Let user add their favorite apps"""
    # Show instruction message in cyan
    print(f"\n{Fore.CYAN}Now, let's set up your 3 favorite apps that will be subject to locking/unlocking:{Style.RESET_ALL}")
    # Loop 3 times to get 3 apps
    for i in range(3):
        # Ask for each app name with cyan prompt
        app_name = input(f"{Fore.CYAN}Enter favorite app #{i+1}: {Style.RESET_ALL}")
        # Add the app to user's favorite apps list
        user.add_favorite_app(app_name)
    # Add blank line for spacing
    print()

def setup_mode(user):
    """Let user choose between reward and punishment mode"""
    # Display mode selection header in cyan
    print(f"\n{Fore.CYAN}Choose your habit enforcement mode:{Style.RESET_ALL}")
    # Show reward mode description in yellow
    print(f"{Fore.YELLOW}1. Reward Mode - Apps start locked and get unlocked as you complete tasks")
    # Show punishment mode description in yellow
    print(f"2. Punishment Mode - Apps start unlocked but get locked if you fail tasks{Style.RESET_ALL}")
    
    # Keep asking until valid choice is made
    while True:
        # Get user's choice with cyan prompt
        choice = input(f"{Fore.CYAN}Choose mode (1/2): {Style.RESET_ALL}")
        if choice == "1":
            # Set reward mode
            user.set_mode("reward")
            # Show confirmation in green
            print(f"{Fore.GREEN}All apps are locked. Complete tasks to unlock them!{Style.RESET_ALL}\n")
            break
        elif choice == "2":
            # Set punishment mode
            user.set_mode("punishment")
            # Show confirmation in yellow
            print(f"{Fore.YELLOW}All apps are unlocked. Don't miss your tasks!{Style.RESET_ALL}\n")
            break
        else:
            # Show error message in red for invalid input
            print(f"{Fore.RED}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}")

def show_menu(user):
    """Display main menu and handle user choices"""
    # Create motivation object for quotes
    motivation = Motivation()
    
    # Keep showing menu until user exits
    while True:
        # Display all menu options in cyan
        print(f"\n{Fore.CYAN}1. Add another habit")
        print("2. View habits")
        print("3. Check goal completion")
        print("4. View app status")
        print("5. Get motivation")
        print(f"6. Exit{Style.RESET_ALL}")
        
        # Get user's menu choice
        choice = input(f"{Fore.CYAN}Choose an option (1-6): {Style.RESET_ALL}")
        
        if choice == "1":
            # Create new habit and add to user's list
            habit = createHabit()
            user.add_habit(habit)
        
        elif choice == "2":
            # Show all user's habits
            print(f"\n{Fore.YELLOW}Your Habits:{Style.RESET_ALL}")
            for habit in user.habits:
                # Display each habit's details with colors
                print(f"{Fore.CYAN}{habit.name} - {habit.habit_type.upper()}")
                print(f"  Period: {habit.start_date} to {habit.end_date}")
                print(f"  Current streak: {Fore.GREEN}{habit.streak} days{Style.RESET_ALL}\n")
        
        elif choice == "3":
            # Check if user has any habits
            if not user.habits:
                print(f"{Fore.RED}No habits added yet!{Style.RESET_ALL}")
                continue
            
            # Show list of habits to check
            print(f"\n{Fore.YELLOW}Check Goal Completion:{Style.RESET_ALL}")
            for i, habit in enumerate(user.habits, 1):
                print(f"{Fore.CYAN}{i}. {habit.name}{Style.RESET_ALL}")
            
            try:
                # Get habit selection from user
                choice = int(input(f"{Fore.CYAN}Select habit to check (number): {Style.RESET_ALL}"))
                habit = user.habits[choice-1]
                # Check if habit was completed
                completed = habit.check_goal_completion()
                if completed:
                    # Update app locks and show success message
                    user.update_app_locks(completed)
                    print(f"{Fore.GREEN}Great job! Your streak is now {habit.calculate_streak()} days.{Style.RESET_ALL}")
                else:
                    # Update app locks and show encouragement message
                    user.update_app_locks(completed)
                    print(f"{Fore.YELLOW}Keep trying! Tomorrow is a new day.{Style.RESET_ALL}")
                
                # Show next check reminder
                next_check = (datetime.now() + timedelta(days=1)).strftime('%A, %B %d')
                print(f"\n{Fore.CYAN}⏰ Reminder: Next check scheduled for {next_check}{Style.RESET_ALL}")
                # Show motivational quote
                motivation.get_motivation()
                
            except (ValueError, IndexError):
                # Show error for invalid selection
                print(f"{Fore.RED}Invalid selection!{Style.RESET_ALL}")
        
        elif choice == "4":
            # Show total completed goals
            print(f"\n{Fore.GREEN}You've completed {user.completed_goals} goals so far!{Style.RESET_ALL}")
            # Show status of all apps
            print(f"\n{Fore.CYAN}App Status ({user.mode.capitalize()} Mode):{Style.RESET_ALL}")
            for app in user.favorite_apps:
                if app in user.locked_apps:
                    # Show locked apps in red
                    print(f"  {Fore.RED}🔒 {app} (LOCKED){Style.RESET_ALL}")
                else:
                    # Show unlocked apps in green
                    print(f"  {Fore.GREEN}🔓 {app} (UNLOCKED){Style.RESET_ALL}")
        
        elif choice == "5":
            # Show motivational quote
            motivation.get_motivation()
        
        elif choice == "6":
            # Show goodbye message and exit
            print(f"{Fore.YELLOW}Thank you for using Habit Haven!{Style.RESET_ALL}")
            break
        
        else:
            # Show error for invalid menu choice
            print(f"{Fore.RED}Invalid choice. Please select 1-6.{Style.RESET_ALL}")

def main():
    """Main program flow"""
    # Get user logged in
    user = login()
    
    # Start habit creation process
    print("Let's start by adding a habit to track:")
    habit = createHabit()
    user.add_habit(habit)
    
    # Allow adding more habits
    while True:
        more = input("\nDo you want to add another habit? (y/n): ").lower()
        if more == 'n':
            break
        elif more == 'y':
            habit = createHabit()
            user.add_habit(habit)
        else:
            print("Please enter 'y' or 'n'")
    
    # Setup apps and mode
    setup_apps(user)
    setup_mode(user)
    
    # Start main menu loop
    show_menu(user)

# Start the program if this file is run directly
if __name__ == "__main__":
    main()