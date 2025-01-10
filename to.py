from datetime import datetime

# Add Task Function
def add_task(tasks, task_name, deadline):
    tasks[task_name.lower()] = {"deadline": deadline, "completed": False}
    print(f"Added: {task_name} (Deadline: {deadline})")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        for name, details in tasks.items():
            status = "Completed" if details["completed"] else "Pending"
            print(f"{name.title()} | Deadline: {details['deadline']} | Status: {status}")

# Mark a task as complete
def mark_complete(tasks, task_name):
    name = task_name.lower()
    if name in tasks:
        tasks[name]["completed"] = True
        print(f"Marked as complete: {task_name}")

        deadline = datetime.strptime(tasks[name]["deadline"], "%d.%m.%y")
        now = datetime.now()
        if now > deadline:
            print("Missed the deadline. work harder!")
        else:
            print("Well done! Completed on time!")
    else:
        print("Task not found!")

# Delete a task
def delete_task(tasks, task_name):
    if tasks.pop(task_name.lower(), None):
        print(f"Deleted: {task_name}")
    else:
        print("Task not found!")

# View overdue tasks
def view_overdue(tasks):
    now = datetime.now()
    overdue_tasks = [name for name, details in tasks.items() if not details["completed"] and datetime.strptime(details["deadline"], "%d.%m.%y") < now]

    if overdue_tasks:
        print("Overdue tasks:")
        for name in overdue_tasks:
            print(name.title())
    else:
        print("No overdue tasks!")

# Main function
def main():
    tasks = {}
    
    while True:
        print("\n1. Add Task  2. View Tasks  3. Mark Complete  4. Delete Task  5. View Overdue  6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Task name: ")
            deadline = input("Deadline (DD.MM.YY): ")
            add_task(tasks, task_name, deadline)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_name = input("Task to mark complete: ")
            mark_complete(tasks, task_name)
        elif choice == "4":
            task_name = input("Task to delete: ")
            delete_task(tasks, task_name)
        elif choice == "5":
            view_overdue(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
