import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    tasks = load_tasks()
    task_id = 1 if not tasks else tasks[-1]['id'] + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")


def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully")


def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return
    print("Task not found")


def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")


# def show_help():
#     print("\nUsage: task-cli <command> [arguments]\n")
#     print("Available commands:")
#     print("  add \"Task Description\"    -> Menambahkan tugas baru")
#     print("  list                      -> Menampilkan semua tugas")
#     print("  list done                 -> Menampilkan tugas yang sudah selesai")
#     print("  list todo                 -> Menampilkan tugas yang belum dikerjakan")
#     print("  list in-progress          -> Menampilkan tugas yang sedang dikerjakan")
#     print("  update <id> \"New Description\" -> Memperbarui deskripsi tugas")
#     print("  delete <id>               -> Menghapus tugas")
#     print("  mark-in-progress <id>     -> Menandai tugas sebagai sedang dikerjakan")
#     print("  mark-done <id>            -> Menandai tugas sebagai selesai")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]
    if command == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif command == "update" and len(sys.argv) >= 4:
        update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif command == "delete" and len(sys.argv) >= 3:
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress" and len(sys.argv) >= 3:
        mark_task(int(sys.argv[2]), "in-progress")
    elif command == "mark-done" and len(sys.argv) >= 3:
        mark_task(int(sys.argv[2]), "done")
    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print("Invalid command or arguments\n")
        show_help()


if __name__ == "__main__":
    main()