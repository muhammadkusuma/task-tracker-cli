# Task Tracker CLI  

Task Tracker is a simple Command Line Interface (CLI) application for tracking and managing your tasks. This application allows you to add, update, delete, and set task statuses easily using terminal commands.  

## 📌 Features  

- Add new tasks  
- Update task descriptions  
- Delete tasks  
- Mark tasks as "in progress" or "done"  
- List all tasks  
- List tasks by status (todo, in-progress, done)  

## 🚀 How to Use  

Make sure you have Python installed on your system. Then, run the following commands:  

### Add a New Task  
```powershell
python script.py add "Buy vegetables at the market"
```

### List All Tasks  
```powershell
python script.py list
```

### Mark a Task as In Progress  
```powershell
python script.py mark-in-progress 1
```

### Mark a Task as Done  
```powershell
python script.py mark-done 1
```

### Update Task Description  
```powershell
python script.py update 1 "Buy vegetables and fruits at the market"
```

### Delete a Task  
```powershell
python script.py delete 1
```

## 📂 Data Storage  
All tasks are automatically saved in the `tasks.json` file, ensuring that your tasks persist even after exiting the program.  

## 🔗 Project URL  
GitHub Repository: [GitHub repository](https://github.com/muhammadkusuma/task-tracker-cli)  
Roadmap: [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker)  

