import time
import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def track_task(tasks):
    print("\n--- Track a Task ---")
    task_name = input("What are you working on? ")
    task_type = input("Is this productive or distracting? (p/d): ")
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    duration = round((end - start) / 60, 2)
    task = {
        "task": task_name,
        "type": "productive" if task_type == "p" else "distracting",
        "minutes": duration,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"\nDone! You spent {duration} minutes on {task_name}")

def show_summary(tasks):
    if not tasks:
        print("\nNo tasks tracked yet!")
        return
    productive = sum(t["minutes"] for t in tasks if t["type"] == "productive")
    distracting = sum(t["minutes"] for t in tasks if t["type"] == "distracting")
    total = productive + distracting
    if total > 0:
        score = round((productive / total) * 100, 1)
    else:
        score = 0
    print("\n--- Your Summary ---")
    print(f"Productive minutes: {productive}")
    print(f"Distracting minutes: {distracting}")
    print(f"Productivity score: {score}%")
    if score >= 70:
        print("Great job! You are staying focused!")
    elif score >= 40:
        print("Not bad, but try to reduce distractions!")
    else:
        print("You need to focus more today!")

def view_history(tasks):
    if not tasks:
        print("\nNo tasks tracked yet!")
        return
    print("\n--- Your History ---")
    for t in tasks:
        label = "productive" if t["type"] == "productive" else "distracting"
        print(f"{t['date']} | {t['task']} | {t['minutes']} mins | {label}")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== Digital Distraction Tracker ===")
        print("1. Track a task")
        print("2. Show summary")
        print("3. View history")
        print("4. Quit")
        choice = input("\nChoose: ")
        if choice == "1":
            track_task(tasks)
        elif choice == "2":
            show_summary(tasks)
        elif choice == "3":
            view_history(tasks)
        elif choice == "4":
            print("\nGoodbye! Keep staying focused!")
            break
        else:
            print("Invalid choice, try again!")

main()
