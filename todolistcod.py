tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def update_task():
    index = int(input("Enter task index to update: ")) - 1
    task = input("Enter updated task: ")
    tasks[index] = task
    print("Task updated!")

def delete_task():
    index = int(input("Enter task index to delete: ")) - 1
    tasks.pop(index)
    print("Task deleted!")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()