from goal import Goal
from array import array

def add_goal(goals):
    title = input("Enter goal: ")
    category = input("Enter category: ")
    deadline = input("Enter deadline: ")

    if title.strip() == "" or category.strip() == "" or deadline.strip() == "":
        print("Please enter all details.")
        return

    if "|" in title or "|" in category or "|" in deadline:
       print("Please do not use the | symbol.")
       return

    goal = Goal(title, category, deadline)
    goals.append(goal)

    print("Goal added successfully!")

def view_goals(goals):
    if not goals:
        print("No goals available.")
        return

    print("\nYour Goals:")

    for number, goal in enumerate(goals, 1):
        print(number, end=". ")
        goal.display()


def complete_goal(goals):
    if not goals:
        print("No goals available.")
        return

    view_goals(goals)

    try:
        number = int(input("Enter goal number to complete: "))

        if 1 <= number <= len(goals):
         selected_goal = goals[number - 1]

         if selected_goal is not None:
              selected_goal.complete()
              print("Goal completed!")
        else:
            print("Invalid goal number.")

    except ValueError:
        print("Please enter a number.")

def show_progress(goals):
    if not goals:
        print("No goals available.")
        return

    progress = array('i', [])

    for goal in goals:
        if goal.completed:
            progress.append(1)
        else:
            progress.append(0)

    completed = sum(progress)
    total = len(progress)
    pending = total - completed
    percentage = (completed / total) * 100

    remaining_goals = total % 2
    half_goals = total // 2


    print("Type of total:", type(total))
    print("\n===== PROGRESS =====")
    print("Total Goals:", total)
    print("Completed Goals:", completed)
    print("Pending Goals:", pending)
    print("Progress:", percentage, "%")
    print("Remaining after pairs:", remaining_goals)
    print("Half of total goals:", half_goals)

def delete_goal(goals):
    if not goals:
        print("No goals available.")
        return

    view_goals(goals)

    try:
        number = int(input("Enter goal number to delete: "))

        if 1 <= number <= len(goals):
            goals.pop(number - 1)
            print("Goal deleted successfully!")
        else:
            print("Invalid goal number.")

    except ValueError:
        print("Please enter a number.")