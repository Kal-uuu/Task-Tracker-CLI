import os
import json
import datetime

task_file = "todo_list"
created_date = datetime.datetime.now()


# check if task file exist
def ensure_file_exist():
    if not os.path.exists(task_file):
        with open(task_file, "w") as file:
            json.dump([], file)


# Loads information from file
def load_file():
    ensure_file_exist()
    with open(task_file, "r") as file:
        try:
            tasks = json.load(file)

            if tasks is None:
                return []
            return tasks
        except json.JSONDecodeError:
            return []


# Saves changes made to the file
def save_file(task):
    with open(task_file, "w") as file:
        json.dump(task, file, indent=4)


# Add a new task
def add_todo(description):
    tasks = load_file()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "TODO",
        "createdAt": created_date.strftime("%m/%d/%Y")
    }
    tasks.append(task)
    save_file(tasks)


# Updates task
def update_task(task_id, description):
    tasks = load_file()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            save_file(tasks)
            print(f"Task {task_id} successfully updated")
            return
    print(f'Task {task_id} does not exist')


# Deletes task
def delete_task(todo_id):
    tasks = load_file()
    for task in tasks:
        if task["id"] == todo_id:
            tasks.remove(task)
            save_file(tasks)
            print(f'Task {todo_id} has been deleted')
            return
    print(f'Task {todo_id} does not exist')


# Updates mark of the task
def update_status(task_id, status):
    tasks = load_file()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status.upper()
            save_file(tasks)
            print(f"Task is now {status}")
            return
    print(f"Task {task_id} does not exist")


# list all the task
def list_all():
    tasks = load_file()
    for task in tasks:
        print(task)


# list task according to the mark
def list_by_status(status):
    tasks = load_file()
    found_tasks = False

    for task in tasks:
        if task["status"].lower() == status.lower():
            print(task)
            found_tasks = True

    if not found_tasks:
        return f"No task found with status '{status}'"
