import json, sys, datetime
from pathlib import Path

def read_json():
    if (not Path('tasks.json').exists()):
        Path('tasks.json').touch()
        return {'tasks': []}
    else:
        with open('tasks.json', encoding='utf-8') as f:
            return json.load(f)
   
def write_json(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def list(rango): 
    tasks = read_json()
    if (rango == 'all'):
        for task in tasks:
            print(task, tasks[task])
    else:
        for task in tasks:
            if (tasks[task] == rango):
                print(task)

def add():
    tasks = read_json()
    task = {'id': 1,
            'description': args[2],
            'status': 'todo',
            'create_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now()
    }
    
    tasks['tasks'].push(task)
    write_json(tasks)

def get_key(tasks):
    index = 1
    keys = tasks.keys()
    if (len(keys) >= int(args[2])):
        for task in tasks:
            if (index == int(args[2])):
                break
            index += 1
        return task
    
    print('El valor ingresado supera la cantidad de elementos')
    return

def delete():
    tasks = read_json()
    key = get_key(tasks)
    if (key):
        del tasks[key]
        write_json(tasks)

def mark_done():
    print('hrllo')

def mark_in_progress():
    print('hrllo')

def update():
    tasks = read_json()
    key = get_key(tasks)
    tasks[args[3]] = tasks[key]
    del tasks[key]
    write_json(tasks)
    

args = sys.argv

    
if (len(args) == 2):
    list('all')

if (len(args) == 3):
    if (args[1] == 'add'):
        add()
    if (args[1] == 'delete'):
        delete()
    if (args[1] == 'list'):
        list(args[2])
    if (args[1] == 'mark-done'):
        mark_done()
    if (args[1] == 'mark-in-progress'):
        mark_in_progress()

if (len(args) == 4):
    update()