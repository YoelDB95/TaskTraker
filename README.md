# Task Tracker
Solution for the challenge from [roadmap.sh](https://roadmap.sh/projects/task-tracker)

# How to run it
Clone the repository and run this commands


Adding a new task
```
python task-cli.py add "Buy groceries"
```

Updating and deleting tasks
```
python task-cli.py update 1 "Buy groceries and cook dinner"
python task-cli.py delete 1
```

Marking a task as in progress or done
```
python task-cli.py mark-in-progress 1
python task-cli.py mark-done 1
```

Listing all tasks

```
python task-cli.py list
```

Listing tasks by status
```
python task-cli.py list done
python task-cli.py list todo
python task-cli.py list in-progress
```