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

task1_thread = threading.Thread(target=put_lettuce_in_fridge, args=[robots[0]])
task2_thread = threading.Thread(target=put_tomato_in_fridge, args=[robots[2]])

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()
