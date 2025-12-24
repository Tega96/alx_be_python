"""
Docstring for alx_be_python.control-flow.daily_reminder

Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.
"""

# Prompt for a single task
task = input("Input a task description: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        print("Priority not valid")

# Modify task if it's time bound
if time_bound == "yes":
    reminder += ' that requires immediate attention today!'
    print(f"Reminder: {reminder}")
elif time_bound == "no":
    reminder += ' that does not necessarily require your immediate attention'
    print(f"Note: {reminder}")