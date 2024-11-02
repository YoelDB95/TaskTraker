import json, sys, datetime
from pathlib import Path

def read_json():
    if (not Path('tasks.json').exists()):
        Path('tasks.json').touch()
        write_json({'tasks': []})

    try:
        with open('tasks.json', encoding='utf-8') as f:
            return json.load(f)
    except IOError as e:
        print(str(e))
   
def write_json(tasks):
    try:
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f)
    except IOError as e:
        print(e)

def list(filter): 
    tasks = read_json()
    
    if (filter == 'none'):
        print('These are all your tasks')
        for task in tasks['tasks']:
            print(task)
    else:
        print(f'These are all your tasks {filter}')
        for task in tasks['tasks']:
            if (task['status'] == filter):
                print(task)

def add():
    tasks = read_json()
    length = len(tasks['tasks']) - 1
    id = tasks['tasks'][length]['id'] + 1
    task = {'id': id,
            'description': args[2],
            'status': 'todo',
            'create_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks['tasks'].append(task)
    write_json(tasks)
    print(f'Task added successfully (ID: {id})')

def get_index(tasks):
    index = 0
    
    for task in tasks['tasks']:
        if (task['id'] == int(args[2])):
            break
        index += 1
    return index if index < len(tasks['tasks']) else -1

def delete(tasks, index):
    del tasks['tasks'][index]
    write_json(tasks)
    print(f'Task deleted successfully (ID: {index})')

def update(tasks, index):
    tasks['tasks'][index]['description'] = args[3]
    tasks['tasks'][index]['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_json(tasks)
    print(f'Task updated successfully (ID: {index})')

def mark(tasks, index, status):
    tasks['tasks'][index]['status'] = status
    write_json((tasks))
    print(f'Task modified successfully (ID: {id})')


def modify(option):
    tasks = read_json()
    index = get_index(tasks)
    if (index < 0):
        print('No existe la tarea')
        return
    
    if (option == 'update'):
        update(tasks, index)
    elif (option == 'delete'): 
        delete(tasks, index)
    elif (option == 'done'):
        mark(tasks, index, 'done')
    elif (option == 'in-progress'):
        mark(tasks, index, 'in-progress')

args = sys.argv

if (len(args) == 2 and args[1] == 'list'):
    list('none')

if (len(args) == 3):
    if (args[1] == 'add'):
        add()
    if (args[1] == 'delete'  and isinstance(args[2],int)):
        modify('delete')
    if (args[1] == 'list'):
        list(args[2])
    if (args[1] == 'mark-done' and isinstance(args[2],int)):
        modify('done')
    if (args[1] == 'mark-in-progress'  and isinstance(args[2],int)):
        modify('in-progress')

if (len(args) == 4 and args[1] == 'update' and isinstance(args[2],int)):
    modify('update')