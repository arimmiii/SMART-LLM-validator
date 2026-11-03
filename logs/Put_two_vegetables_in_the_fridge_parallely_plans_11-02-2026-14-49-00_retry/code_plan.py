def put_lettuce_in_fridge(robot):
    # SubTask 1: Put Lettuce in the fridge
    GoToObject(robot, 'Lettuce')
    PickupObject(robot, 'Lettuce')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Lettuce', 'Fridge')
    CloseObject(robot, 'Fridge')

def put_tomato_in_fridge(robot):
    # SubTask 2: Put Tomato in the fridge
    GoToObject(robot, 'Tomato')
    PickupObject(robot, 'Tomato')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Tomato', 'Fridge')
    CloseObject(robot, 'Fridge')

# Create threads for each task using Robot 1 for Lettuce and Robot 3 for Tomato
robot_for_lettuce = robots[0] # Using Robot 1 for Lettuce
robot_for_tomato = robots[2] # Using Robot 3 for Tomato

# Create threads for both subtasks
lettuce_thread = threading.Thread(target=put_lettuce_in_fridge, args=(robot_for_lettuce,))
tomato_thread = threading.Thread(target=put_tomato_in_fridge, args=(robot_for_tomato,))

# Start executing both subtasks in parallel
lettuce_thread.start()
tomato_thread.start()

# Wait for both threads to finish
lettuce_thread.join()
tomato_thread.join()
