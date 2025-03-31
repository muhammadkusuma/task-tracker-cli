# Task Tracker CLI

Task Tracker CLI is a simple command-line tool for tracking and managing tasks. It allows users to add, update, delete, and manage task statuses efficiently using a JSON-based storage system.

## Project URL
[GitHub Repository](https://github.com/muhammadkusuma/task-tracker-cli)

## Features
- Add new tasks
- Update task descriptions
- Delete tasks
- Mark tasks as in progress or done
- List all tasks or filter by status
- JSON-based storage for persistence

## Installation
Clone this repository and navigate into the directory:

```sh
git clone https://github.com/muhammadkusuma/task-tracker-cli.git
cd task-tracker-cli
```

Ensure you have Python installed, then run:

```sh
python script.py
```

## Usage
Run the following commands to interact with the Task Tracker CLI:

### Add a Task
```sh
python script.py add "Buy groceries"
```

### Update a Task
```sh
python script.py update 1 "Buy groceries and cook dinner"
```

### Delete a Task
```sh
python script.py delete 1
```

### Mark a Task as In Progress
```sh
python script.py mark-in-progress 1
```

### Mark a Task as Done
```sh
python script.py mark-done 1
```

### List All Tasks
```sh
python script.py list
```

### List Tasks by Status
```sh
python script.py list done
python script.py list todo
python script.py list in-progress
```

## File Storage
Tasks are stored in `tasks.json` in the same directory as `script.py`. The JSON file structure follows:
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2025-03-31T12:00:00",
    "updatedAt": "2025-03-31T12:00:00"
  }
]
```

## Contributing
Feel free to fork this repository and submit pull requests for improvements.

## License
This project is licensed under the MIT License.