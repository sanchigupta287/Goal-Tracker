# Goal & Habit Tracker CLI

## 1. Project Overview
The **Goal & Habit Tracker CLI** is a lightweight Python-based command-line interface application designed to help first-year university students set, track, and monitor their academic and personal goals. Built as a term project for CSE1021 (Introduction to Problem Solving and Programming), it applies core programming concepts such as file I/O operations, list and dictionary manipulation, modular function architecture, and user input validation.

---

## 2. Features
- **Goal Management (CRUD):** Add new goals with categories (e.g., Academic, Fitness) and view active goals.
- **Progress Tracking:** Dynamically update progress percentage (0–100%) and auto-mark tasks as "Completed" when reaching 100%.
- **Persistent Data Storage:** Automatically loads and saves goal records to a local `goals.txt` storage file so data persists across sessions.
- **Progress Analytics Module:** Calculates total goals tracked, count of completed vs. in-progress tasks, and overall average completion rate.
- **Error Handling:** Robust input validation using `try-except` blocks to prevent crashes on invalid menu options or integer entries.

---

## 3. Technologies & Tools Used
- **Programming Language:** Python 3.x
- **Core Concepts:** Data Structures (Lists & Dictionaries), File Handling, Control Flow, Functions
- **Development Tools:** Google Colab 
- **Version Control:** Git & GitHub

---

## 4. How to Run in Google Colab
1. Open [Google Colab](https://colab.research.google.com/).
2. Create a new notebook or upload your script.
3. Paste the code from `tracker.py` into a code cell.
4. Click the **Play button** (or press `Shift + Enter`) to run the program.
5. Interact with the CLI menu directly inside the output panel below the cell.

---

## 5. Instructions for Testing
To test all functions in the program, run the code cell in Colab and perform the following sequence[cite: 2]:

1. **Add Goals (Option 1):**
   - Enter `1`. Set Title: `"Run 10000 steps"`, Category: `"Fitness"`.
   - Enter `1`. Set Title: `"English Assignment"`, Category: `"Academic"`.
2. **View Goals (Option 2):**
   - Enter `2` to view both added goals with progress initialized at `0%`.
3. **Update Progress (Option 3):**
   - Enter `3`. Select Goal ID `1` and set progress to `100%` (Status updates to `"Completed"`).
   - Enter `3`. Select Goal ID `2` and set progress to `50%`.
4. **View Analytics (Option 4):**
   - Enter `4` to check summary metrics (Total Goals: 2, Completed: 1, Average Progress: 75.0%).
5. **Exit (Option 5):**
   - Enter `5` to terminate the program safely.

---

## 6. Project Directory Structure
```text
Goal-Tracker/
│
├── tracker.py         # Core Python source code
├── statement.md       # Problem statement, target users, and scope
├── goals.txt          # Saved goal records (data persistence)
└── README.md          # Project documentation and user guide
