import json, sys, datetime
from pathlib import Path

def read_json():
    if (not Path('tasks.json').exists()):
        Path('tasks.json').touch()
        write_json({'tasks': []})

    with open('tasks.json', encoding='utf-8') as f:
        return json.load(f)
   
def write_json(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def list(filter): 
    tasks = read_json()
    if (filter == 'none'):
        for task in tasks['tasks']:
            print(task)
    else:
        for task in tasks:
            if (task['status'] == filter):
                print(task)

def add():
    tasks = read_json()
    length = len(tasks['tasks']) - 1
    
    task = {'id': tasks['tasks'][length]['id'] + 1,
            'description': args[2],
            'status': 'todo',
            'create_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks['tasks'].append(task)
    write_json(tasks)

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

def update(tasks, index):
    tasks['tasks'][index]['description'] = args[3]
    tasks['tasks'][index]['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_json(tasks)

def mark(tasks, index, status):
    tasks['tasks'][index]['status'] = status
    write_json((tasks))


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

if (len(args) == 2):
    list('none')

if (len(args) == 3):
    if (args[1] == 'add'):
        add()
    if (args[1] == 'delete'):
        modify('delete')
    if (args[1] == 'list'):
        list(args[2])
    if (args[1] == 'mark-done'):
        modify('done')
    if (args[1] == 'mark-in-progress'):
        modify('in-progress')

if (len(args) == 4):
    modify('update')