import time
from datetime import datetime

# Add a new to-do task
def add_task(tasks, task_name, deadline):
    tasks[task_name.lower()] = {
        "deadline": deadline,
        "completed": False
    }
    print(f"Task added: {task_name} with deadline {deadline}")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
        return

    for task_name, details in tasks.items():
        status = "Completed" if details["completed"] else "Pending"
        print(f"Task: {task_name} | Deadline: {details['deadline']} | Status: {status}")

def mark_task_complete(tasks, task_name):
    """
    Mark a task as done and check if it was finished on time.

    Args:
        tasks (dict): A dictionary of tasks.
        task_name (str): The name of the task to mark as complete.
    """
    task_name = task_name.lower()
    if task_name in tasks:
        tasks[task_name]["completed"] = True
        print(f"Task marked as complete: {task_name}")

        # Check if the task is completed after the deadline
        current_time = datetime.now()
        task_deadline = datetime.strptime(tasks[task_name]["deadline"], "%d.%m.%y")
        if current_time > task_deadline:  # Missed deadline
            print(f"Sorry, good job but , you've missed the deadline, try to work harder next time.")
        elif current_time == task_deadline:  # Completed exactly on the deadline
            print(f"Congratulations! You finished the task '{task_name}' just in time!")
        else:  # Completed before the deadline
            print(f"Great job! Task '{task_name}' was completed before the deadline!")
    else:
        print(f"Task not found: {task_name}")

# Delete a task
def delete_task(tasks, task_name):
    task_name = task_name.lower()
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task deleted: {task_name}")
    else:
        print(f"Task not found: {task_name}")

# View overdue tasks
def view_overdue_tasks(tasks):
    current_time = datetime.now()
    overdue_found = False

    for task_name, details in tasks.items():
        task_deadline = datetime.strptime(details["deadline"], "%d.%m.%y")
        if not details["completed"] and task_deadline < current_time:
            print(f"Overdue Task: {task_name} | Deadline: {details['deadline']}")
            overdue_found = True

    if not overdue_found:
        print("No overdue tasks!")

# Main function
def main():
    tasks = {}

    while True:
        print("\nTo-Do Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. View overdue tasks")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            deadline = input("Enter deadline (DD.MM.YY): ")
            add_task(tasks, task_name, deadline)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            task_name = input("Enter task name to mark as complete: ")
            mark_task_complete(tasks, task_name)

        elif choice == "4":
            task_name = input("Enter task name to delete: ")
            delete_task(tasks, task_name)

        elif choice == "5":
            view_overdue_tasks(tasks)

        elif choice == "6":
            print("Exiting To-Do Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
