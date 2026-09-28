class Goal:
    def __init__(self, title, category, deadline):
        self.title = title
        self.category = category
        self.deadline = deadline
        self.completed = False

    def complete(self):
        self.completed = True

    def display(self):
        status = "Completed" if self.completed else "Pending"

        print(
            self.title,
            "|",
            self.category,
            "|",
            self.deadline,
            "|",
            status
        )