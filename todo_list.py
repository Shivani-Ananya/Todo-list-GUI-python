import json
import os

if not os.path.exists("todo_list.json") or os.stat("todo_list.json").st_size == 0:
    with open("todo_list.json", "w") as file:
        json.dump([], file)

while True:
    print("\n==== Options =====")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Update a log")
    print("5. Delete task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()
    

    if choice == "1":
        user_task = input("Enter Your Task: ")

        task = {
            "task": user_task,
            "status": False
            }
    with open("todo_list.json", "r") as file:
        tasks = json.load(file)

    tasks.append(new_task)

    with open("todo_list.json", "w") as file:
        json.dump(tasks, file, indent=2)
        print("Task added successfully!")


        
    elif choice == "2":
    with open("todo_list.json", "r") as file:
        tasks = json.load(file)

    if not tasks:
        print("No Tasks Yet!")
    else:
        print("\n--- Tasks Found ---")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["status"] else "Not Done"
            print(f"[{i}] {status} {task['task']}")


            
    elif choice == "3":
    with open("todo_list.json", "r") as file:
        tasks = json.load(file)

    if not tasks:
        print("No tasks available to mark!")
    else:
        print("\n--- Tasks ---")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["status"] else "Not Done"
            print(f"[{i}] {status} {task['task']}")

        try:
            task_num = int(input("Enter the task number to mark as completed: "))

            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["status"] = True
                
                with open("todo_list.json", "w") as file:
                    json.dump(tasks, file, indent=2)
                print(f'Task "{tasks[task_num - 1]["task"]}" marked as completed')
                
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


        
    elif choice == "4":
    with open("todo_list.json", "r") as file:
        tasks = json.load(file)

    if not tasks:
        print("No tasks available to update!")
    else:
        print("\n--- Tasks ---")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["status"] else "Not Done"
            print(f"[{i}] {status} {task['task']}")

        try:
            to_update = int(input("Enter the task number to update: "))

            if 1 <= to_update <= len(tasks):
                update_dets = input("Enter the new task details: ").strip()

                if update_dets:
                    tasks[to_update - 1]["task"] = update_dets

                    with open("todo_list.json", "w") as file:
                        json.dump(tasks, file, indent=2)
                    print("Task updated successfully!")
                    
                else:
                    print("No details entered. Update cancelled.")
                    
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

  
        
   elif choice == "5":
    with open("todo_list.json", "r") as file:
        tasks = json.load(file)

    if not tasks:
        print("No tasks available to delete!")
    else:
        print("\n--- Tasks ---")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["status"] else "Not Done"
            print(f"[{i}] {status} {task['task']}")

        try:
            to_delete = int(input("Enter the task number to delete: "))

            if 1 <= to_delete <= len(tasks):
                confirm = input(f"Are you sure you want to delete task '{tasks[to_delete - 1]['task']}'? (y/n): ").strip().lower()
                if confirm == 'y':
                    deleted_task = tasks.pop(to_delete - 1)
                    with open("todo_list.json", "w") as file:
                        json.dump(tasks, file, indent=2)
                    print(f"Task '{deleted_task['task']}' deleted successfully!")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "6":
        print("Thank you for using your To-Do List app! Stay productive!")
        break
