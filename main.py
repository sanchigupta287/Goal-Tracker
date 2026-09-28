from functions import add_goal, view_goals, complete_goal, show_progress, delete_goal
from storage import load_goals, save_goals


goals = load_goals()


while True:

    print("\n===== PERSONAL GOAL TRACKER =====")
    print("1. Add Goal")
    print("2. View Goals")
    print("3. Complete Goal")
    print("4. Show Progress")
    print("5. Delete Goal")
    print("6. Exit")
    

    choice = input("Enter your choice: ")

    if choice == "1":
        add_goal(goals)
        save_goals(goals)

    elif choice == "2":
        view_goals(goals)

    elif choice == "3":
        complete_goal(goals)
        save_goals(goals)

    elif choice == "4":
        show_progress(goals)

    elif choice == "5":
        delete_goal(goals)
        save_goals(goals)

    elif choice == "6":
        print("Thank you for using Goal Tracker!")
        break

    else:
        print("Invalid choice.")