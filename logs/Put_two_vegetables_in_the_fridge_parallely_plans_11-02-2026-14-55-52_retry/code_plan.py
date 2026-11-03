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

task_lettuce_thread = threading.Thread(target=put_lettuce_in_fridge, args=(robots[0],))
task_tomato_thread = threading.Thread(target=put_tomato_in_fridge, args=(robots[2],))

task_lettuce_thread.start()
task_tomato_thread.start()

task_lettuce_thread.join()
task_tomato_thread.join()

print("Task: Put Lettuce and Tomato in the fridge is done.")
