import os

# Function to load tasks from a text file
def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = file.read().splitlines()
    return tasks

# Function to save tasks to a text file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Main function to manage the To-Do List
def main():
    filename = 'todo.txt'
    tasks = load_tasks(filename)
    
    while True:
        print("\n===== To-Do List =====")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task as complete")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
            save_tasks(filename, tasks)
        elif choice == '2':
            task_number = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] = "[X] " + tasks[task_number - 1]
                save_tasks(filename, tasks)
            else:
                print("Invalid task number.")
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
                save_tasks(filename, tasks)
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
