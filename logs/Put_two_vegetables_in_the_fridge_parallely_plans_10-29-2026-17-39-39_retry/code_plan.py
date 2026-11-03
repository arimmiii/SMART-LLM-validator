def put_lettuce_in_fridge(robot):
    GoToObject(robot, 'Lettuce')
    PickupObject(robot, 'Lettuce')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Lettuce', 'Fridge')
    CloseObject(robot, 'Fridge')

def put_tomato_in_fridge(robot):
    GoToObject(robot, 'Tomato')
    PickupObject(robot, 'Tomato')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Tomato', 'Fridge')
    CloseObject(robot, 'Fridge')

# Create threads for each subtask using different robots
robot_for_lettuce = robots[0]  # Robot 1
robot_for_tomato = robots[2]   # Robot 3

# Create threads for concurrent execution
lettuce_thread = threading.Thread(target=put_lettuce_in_fridge, args=(robot_for_lettuce,))
tomato_thread = threading.Thread(target=put_tomato_in_fridge, args=(robot_for_tomato,))

# Start executing both subtasks in parallel
lettuce_thread.start()
tomato_thread.start()

# Wait for both subtasks to finish
lettuce_thread.join()
tomato_thread.join()

print("Both Lettuce and Tomato have been successfully put in the fridge.")
