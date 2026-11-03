def slice_apple():
    # 0: SubTask 1: Slice the Apple
    # 1: Go to the Knife using robot1.
    GoToObject(robots[0], 'Knife')
    # 2: Pick up the Knife using robot1.
    PickupObject(robots[0], 'Knife')
    # 3: Go to the Apple using robot1.
    GoToObject(robots[0], 'Apple')
    # 4: Slice the Apple using robot1.
    SliceObject(robots[0], 'Apple')
    # 5: Go to the CounterTop using robot1.
    GoToObject(robots[0], 'CounterTop')
    # 6: Put the Knife back on the CounterTop using robot1.
    PutObject(robots[0], 'Knife', 'CounterTop')

def throw_sliced_apple_in_trash():
    # 0: SubTask 2: Throw the sliced Apple in the trash
    # 1: Go to the GarbageCan using robot2.
    GoToObject(robots[2], 'GarbageCan')
    # 2: Pick up the sliced Apple using robot2.
    PickupObject(robots[2], 'Apple')
    # 3: Throw the sliced Apple in the GarbageCan using robot3.
    ThrowObject(robots[2], 'Apple', 'GarbageCan')

slice_apple()
throw_sliced_apple_in_trash()
