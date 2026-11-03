def slice_bread(robot):
    # SubTask 1: Slice the Bread using Robot #3.
    # 1: Go to the Bread loaf.
    GoToObject(robot, 'Bread')
    # 2: Pick up the Bread.
    PickupObject(robot, 'Bread')
    # 3: Slice the Bread.
    SliceObject(robot, 'Bread')

def toast_bread():
    # SubTask 2: Toast the sliced bread using Robot #2 and Robot #1.
    # 1: Go to the Toaster using Robot #2.
    GoToObject(robots[1], 'Toaster')
    # 2: Put the sliced Bread in the Toaster using Robot #2.
    PutObject(robots[1], 'Bread', 'Toaster')

    # Now toast the bread using Robot #1
    SwitchOn(robots[0], 'Toaster')
    time.sleep(5)  # Wait for a while to let the bread toast
    SwitchOff(robots[0], 'Toaster')

# Execute SubTask 1 with Robot #3 to slice the bread
slice_bread(robots[2])
# Execute SubTask 2 to toast the bread
toast_bread()
