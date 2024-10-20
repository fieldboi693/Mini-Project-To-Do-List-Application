# to_do_list.py

# Welcome Message
def display_welcome():
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# Task Management Functions
def add_task(tasks):
    title = input("Enter the task title: ").strip()
    tasks.append({"title": title, "status": "incomplete"})
    print(f'Task "{title}" added.')

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['title']} - {task['status']}")

def mark_task_complete(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["status"] = "complete"
                print(f'Task "{tasks[task_num - 1]["title"]}" marked as complete.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input, please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                task = tasks.pop(task_num - 1)
                print(f'Task "{task["title"]}" deleted.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input, please enter a number.")

# Main Application Loop
def to_do_list_app():
    tasks = []
    
    while True:
        display_welcome()
        
        try:
            choice = input("Please choose an option (1-5): ").strip()
            
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                mark_task_complete(tasks)
            elif choice == '4':
                delete_task(tasks)
            elif choice == '5':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option, please choose a number between 1 and 5.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            print("\n")

if __name__ == "__main__":
    to_do_list_app()