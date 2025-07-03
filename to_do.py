#1create an item
#2list items
#3mark them as incomplete at first
#4mark them as complete when done
#5save items

import json
filename = "todolist.json"

def load_tasks():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return {"tasks":[]}

def save_tasks(tasks):
    try:
        with open(filename,"w") as file:
            return json.dump(tasks, file)
    except:
        print("Failed to save.")

def view_tasks(tasks):
    task_list = tasks["tasks"]
    if task_list == None or len(task_list) == 0:
        print("No task to display.")
    else:
        print("Your To-Do list:") 
        for index, task in enumerate(task_list):
            status = "Complete" if task.get("Complete", False) else "Pending"
            print(f"{index+1}. {task['description']} | {status}")


def create_task(tasks):
    description = input("Write a task description.")
    if description:
        tasks["tasks"].append({"description": description, "Complete": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Description is necessary. Task creation failed.")

def mark_task_complete(tasks):
    tasks_list = tasks["tasks"]
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task you wish to mark as complete.").strip()) 
        if 1 <= task_number <= len(tasks_list):
            tasks_list[task_number - 1]["Complete"] = True
            print("Task marked as complete.")
        else:
            print("Invalid number.")
    except:
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    tasks_list = tasks["tasks"]
    try:
        task_delete_num = int(input("Which task number would you like to delete?").strip())
        if 1 <= task_delete_num <= len(tasks_list):
            del tasks_list[task_delete_num-1]   
            save_tasks(tasks)
            print("Task deleted successfully")
        else:
            print("Task could not be deleted.")            

    except:
        print("Task could not be deleted.s")

def main():
    tasks = load_tasks()
    while True:
        print("\nThis is a to-do list application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice.").strip()

        # view_tasks(tasks) if choice == "1" else None
        # create_task(tasks) if choice == "2" else None
        # mark_task_complete(tasks) if choice == "3" else None
        # delete_task(tasks) if choice == "4" else None
        # if choice == "5":
        #     break
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid command. Please try again.")


main()