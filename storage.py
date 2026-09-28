from goal import Goal


def save_goals(goals):
    with open("goals.txt", "w") as file:
        for goal in goals:
            file.write(
                goal.title + "|" +
                goal.category + "|" +
                goal.deadline + "|" +
                str(goal.completed) + "\n"
            )


def load_goals():
    goals = []

    try:
        with open("goals.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    goal = Goal(data[0], data[1], data[2])
                    goal.completed = data[3] == "True"
                    goals.append(goal)

    except FileNotFoundError:
        pass

    return goals