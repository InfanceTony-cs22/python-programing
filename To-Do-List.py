# Sample code for a To-Do List Application

# Initialize an empty to-do list
tasks = []

# Function to add a task
def add_task(task_name, description="", due_date=""):
    task = {"name": task_name, "description": description, "due_date": due_date, "completed": False}
    tasks.append(task)

# Function to list all tasks
def list_tasks():
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}. {task['name']} - {task['description']} (Due: {task['due_date']}) - {status}")

# Function to mark a task as completed
def mark_completed(task_index):
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True

# Function to remove a task
def remove_task(task_index):
    if 0 < task_index <= len(tasks):
        del tasks[task_index - 1]

# Main program loop
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Quit")

    choice = input("Enter your choice: ")
#conditional statements
    if choice == "1":
        task_name = input("Enter task name: ")
        description = input("Enter task description (optional): ")
        due_date = input("Enter due date (optional): ")
        add_task(task_name, description, due_date)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        task_index = int(input("Enter the task number to mark as completed: "))
        mark_completed(task_index)
    elif choice == "4":
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
