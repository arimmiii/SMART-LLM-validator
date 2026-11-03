def slice_apple(robot_list):
    # robot_list = [robot1]
    # 0: SubTask 1: Slice the Apple
    # 1: Go to the Knife using robot1.
    GoToObject(robot_list[0], 'Knife')
    # 2: Pick up the Knife using robot1.
    PickupObject(robot_list[0], 'Knife')
    # 3: Go to the Apple using robot1.
    GoToObject(robot_list[0], 'Apple')
    # 4: Slice the Apple using robot1.
    SliceObject(robot_list[0], 'Apple')
    # 5: Go to the CounterTop using robot1.
    GoToObject(robot_list[0], 'CounterTop')
    # 6: Put the Knife back on the CounterTop using robot1's skills is not allowed.

def throw_sliced_apple_in_trash(robot_list):
    # robot_list = [robot2]
    # 0: SubTask 2: Throw the sliced Apple in the trash
    # 1: Go to the sliced Apple using robot2.
    GoToObject(robot_list[0], 'Apple')  
    # 2: Pick up the sliced Apple using robot2.
    PickupObject(robot_list[0], 'Apple')
    # 3: Go to the Trash Can using robot2.
    GoToObject(robot_list[0], 'GarbageCan')
    # 4: Throw the sliced Apple in the Trash Can using robot3.
    PutObject(robot_list[0], 'Apple', 'GarbageCan')

# Execute SubTask 1 with Robot 1
slice_apple([robots[0]])

# Execute SubTask 2 with Robot 2
throw_sliced_apple_in_trash([robots[1]])
