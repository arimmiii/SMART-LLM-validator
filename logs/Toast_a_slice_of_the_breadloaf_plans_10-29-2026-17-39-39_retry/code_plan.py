def retrieve_bread_slice(robot):
    # SubTask 1: Retrieve a slice of bread from the loaf
    # Go to the Bread loaf using robot.
    GoToObject(robot, 'Bread')
    # Pick up a slice of Bread using robot.
    PickupObject(robot, 'Bread')
    # Go to the Toaster using robot.
    GoToObject(robot, 'Toaster')
    # Put the slice of Bread in the Toaster using robot.
    PutObject(robot, 'Bread', 'Toaster')

def toast_bread(robot):
    # SubTask 2: Toast the slice of bread
    # Switch on the Toaster using robot.
    SwitchOn(robot, 'Toaster')
    # Wait for a while to let the bread toast.
    time.sleep(5)  # Adjust time as necessary for toasting
    # Switch off the Toaster using robot.
    SwitchOff(robot, 'Toaster')

# Execute SubTask 1 with Robot 2
retrieve_bread_slice(robots[1])

# Execute SubTask 2 with Robot 1
toast_bread(robots[0])

# Task toast a slice of the bread loaf is done
