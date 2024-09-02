import request
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [Options]")
        return
    command = sys.argv[1]

    if command == "add":
        description = " ".join(sys.argv[2:])
        request.add_todo(description)
    elif command == "update":
        task_id = int(sys.argv[2])
        description = str(" ".join(sys.argv[3:]))
        request.update_task(task_id, description)
    elif command == "delete":
        delete = int(" ".join(sys.argv[2:]))
        request.delete_task(delete)
    elif command == "mark":
        mark_id = ["In-Progress", "Done"]
        task_id = int(sys.argv[2])
        status = str(" ".join(sys.argv[3:]))
        if status not in mark_id:
            print(f"Invalid mark\nMust be '{mark_id[0]} or {mark_id[1]}'")
        request.update_status(task_id, status)
    elif command == "list_all":
        request.list_all()
    elif command == "list_by_status":
        if len(sys.argv) != 3:
            print("Usage: python main.py list_by_status <status>")
        else:
            status = sys.argv[2]
            result = request.list_by_status(status)
            if result:
                print(result)
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
