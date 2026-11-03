import threading

def retrieve_knife(robot):
    # SubTask 1: Retrieve the Knife
    GoToObject(robot, 'Knife')
    PickupObject(robot, 'Knife')

def go_to_tomato(robot):
    # SubTask 2: Go to the Tomato
    GoToObject(robot, 'Tomato')

def slice_tomato(robot):
    # SubTask 3: Slice the Tomato
    SliceObject(robot, 'Tomato')

def put_knife_back(robot):
    # SubTask 4: Put the Knife back on CounterTop
    GoToObject(robot, 'CounterTop')
    PutObject(robot, 'Knife', 'CounterTop')

# Create threads for each subtask
threads = []
robot1 = robots[0]['name']
robot2 = robots[1]['name']
robot3 = robots[2]['name']

# Assigning tasks to robots using threads for parallel execution
threads.append(threading.Thread(target=retrieve_knife, args=(robot1,)))
threads.append(threading.Thread(target=go_to_tomato, args=(robot2,)))
threads.append(threading.Thread(target=slice_tomato, args=(robot3,)))

# Start executing subtasks in parallel
for thread in threads:
    thread.start()

# Wait for all threads to complete before putting knife back
for thread in threads:
    thread.join()

# After slicing is done, put knife back using robot1 or robot2
put_knife_back(robot1) # or put_knife_back(robot2)

# Task slice the tomato is done
