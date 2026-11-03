def slice_apple(robot):
    # 0: SubTask 1: Slice the Apple
    # 1: Go to the Knife.
    GoToObject(robot, 'Knife')
    # 2: Pick up the Knife.
    PickupObject(robot, 'Knife')
    # 3: Go to the Apple.
    GoToObject(robot, 'Apple')
    # 4: Slice the Apple.
    SliceObject(robot, 'Apple')
    # 5: Go to the CounterTop.
    GoToObject(robot, 'CounterTop')
    # 6: Put the sliced Apple on the CounterTop.
    PutObject(robot, 'Apple', 'CounterTop')

def throw_sliced_apple_in_trash(robot):
    # 0: SubTask 2: Throw the sliced Apple in the trash
    # 1: Go to the CounterTop where the sliced Apple is.
    GoToObject(robot, 'CounterTop')  
    # 2: Pick up the sliced Apple.
    PickupObject(robot, 'Apple')
    # 3: Go to the Trash (GarbageCan).
    GoToObject(robot, 'GarbageCan')  
    # 4: Throw the sliced Apple in the trash.
    ThrowObject(robot, 'Apple', 'GarbageCan')

# Execute SubTask 1 with Robot 1
slice_apple(robots[0])

# Execute SubTask 2 with Robot 3 after slicing is done
throw_sliced_apple_in_trash(robots[2])
