import os

DATA_FILE = "goals.txt"

def load_goals():
    """Reads saved goals from goals.txt line by line."""
    goals = []
    if not os.path.exists(DATA_FILE):
        return goals
    
    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 5:
                    goal = {
                        "id": int(parts[0]),
                        "title": parts[1],
                        "category": parts[2],
                        "progress": int(parts[3]),
                        "status": parts[4]
                    }
                    goals.append(goal)
    return goals

def save_goals(goals):
    """Saves updated goals to goals.txt."""
    with open(DATA_FILE, "w") as file:
        for g in goals:
            file.write(f"{g['id']},{g['title']},{g['category']},{g['progress']},{g['status']}\n")

def add_goal(goals):
    """Module 1: Adds a new goal."""
    print("\n--- ADD NEW GOAL ---")
    title = input("Enter Goal Title: ").strip()
    category = input("Enter Category (e.g., Academic, Fitness): ").strip()
    
    goal_id = len(goals) + 1
    new_goal = {
        "id": goal_id,
        "title": title,
        "category": category,
        "progress": 0,
        "status": "In Progress"
    }
    goals.append(new_goal)
    save_goals(goals)
    print(f"✅ Goal '{title}' added successfully!")

def view_goals(goals):
    """Module 2: Displays all tracked goals."""
    print("\n--- YOUR GOALS ---")
    if not goals:
        print("No goals found. Add one first!")
        return
    
    for g in goals:
        print(f"[{g['id']}] {g['title']} | Category: {g['category']} | Progress: {g['progress']}% | Status: {g['status']}")

def update_progress(goals):
    """Module 3: Updates goal progress percentage."""
    view_goals(goals)
    if not goals:
        return
    
    try:
        goal_id = int(input("\nEnter Goal ID to update: "))
        selected = next((g for g in goals if g["id"] == goal_id), None)
        
        if selected:
            new_prog = int(input("Enter new progress percentage (0-100): "))
            if 0 <= new_prog <= 100:
                selected["progress"] = new_prog
                if new_prog == 100:
                    selected["status"] = "Completed"
                save_goals(goals)
                print("✅ Progress updated successfully!")
            else:
                print("⚠️ Invalid percentage. Enter a value from 0 to 100.")
        else:
            print("⚠️ Goal ID not found.")
    except ValueError:
        print("⚠️ Invalid input! Please enter numbers only.")

def view_analytics(goals):
    """Module 4: Generates summary statistics of tracked goals."""
    print("\n--- GOAL ANALYTICS & SUMMARY ---")
    if not goals:
        print("No goals to analyze. Add some goals first!")
        return
    
    total_goals = len(goals)
    completed = sum(1 for g in goals if g["status"] == "Completed")
    in_progress = total_goals - completed
    total_progress = sum(g["progress"] for g in goals)
    avg_progress = total_progress / total_goals
    
    print(f"Total Goals Tracked : {total_goals}")
    print(f"Completed Goals     : {completed}")
    print(f"In-Progress Goals   : {in_progress}")
    print(f"Average Completion  : {avg_progress:.1f}%")

def main():
    goals = load_goals()
    
    while True:
        print("\n==============================")
        print("   GOAL & HABIT TRACKER CLI   ")
        print("==============================")
        print("1. Add New Goal")
        print("2. View All Goals")
        print("3. Update Goal Progress")
        print("4. View Progress Analytics")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            add_goal(goals)
        elif choice == "2":
            view_goals(goals)
        elif choice == "3":
            update_progress(goals)
        elif choice == "4":
            view_analytics(goals)
        elif choice == "5":
            print("Saving data and exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()
