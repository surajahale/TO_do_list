tasks = []

def add_task(description):
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'completed': False
    }
    tasks.append(task)
    print(f"Task added: {description}")

def update_task(task_id, new_description):
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            print(f"Task updated: {new_description}")
            return
    print(f"Task with ID {task_id} not found.")

def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    print(f"Task {task_id} deleted.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = "Completed" if task['completed'] else "Pending"
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {status}")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. View Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to update: "))
                new_description = input("Enter new task description: ")
                update_task(task_id, new_description)
            except ValueError:
                print("Invalid input. Task ID must be a number.")
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to complete: "))
                complete_task(task_id)
            except ValueError:
                print("Invalid input. Task ID must be a number.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid input. Task ID must be a number.")
        elif choice == '5':
            view_tasks()
        elif choice == '6':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
