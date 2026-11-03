def put_lettuce_in_fridge(robot):
    # SubTask for putting Lettuce in fridge
    GoToObject(robot, 'Lettuce')
    PickupObject(robot, 'Lettuce')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Lettuce', 'Fridge')
    CloseObject(robot, 'Fridge')

def put_tomato_in_fridge(robot):
    # SubTask for putting Tomato in fridge
    GoToObject(robot, 'Tomato')
    PickupObject(robot, 'Tomato')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Tomato', 'Fridge')
    CloseObject(robot, 'Fridge')

# Create threads for each subtask with assigned robots
task1_thread = threading.Thread(target=put_lettuce_in_fridge, args=[robots[0]]) # Robot 1 for Lettuce
task2_thread = threading.Thread(target=put_tomato_in_fridge, args=[robots[2]]) # Robot 3 for Tomato

# Start executing both subtasks in parallel
task1_thread.start()
task2_thread.start()

# Wait for both subtasks to finish
task1_thread.join()
task2_thread.join()
