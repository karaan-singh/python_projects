tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    show_tasks()
    try:
        num = int(input("Enter the task number to remove: "))
        removed = tasks.pop(num - 1)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    print("\nOptions: show, add, remove, quit")
    choice = input("Choose an option: ").lower()
    if choice == "show":
        show_tasks()
    elif choice == "add":
        add_task()
    elif choice == "remove":
        remove_task()
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")