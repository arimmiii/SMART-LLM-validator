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

lettuce_robot = robots[0]  # robot1
tomato_robot = robots[2]   # robot3

lettuce_thread = threading.Thread(target=put_lettuce_in_fridge, args=(lettuce_robot,))
tomato_thread = threading.Thread(target=put_tomato_in_fridge, args=(tomato_robot,))

lettuce_thread.start()
tomato_thread.start()

lettuce_thread.join()
tomato_thread.join()
