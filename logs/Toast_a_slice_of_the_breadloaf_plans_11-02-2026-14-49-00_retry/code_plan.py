def retrieve_bread_slice(robot_list):
    # SubTask 1: Retrieve a slice of bread from the loaf
    # Using robot2 to perform this task.
    GoToObject(robot_list[0], 'Bread')          # Robot goes to Bread
    PickupObject(robot_list[0], 'Bread')        # Robot picks up Bread
    GoToObject(robot_list[0], 'Toaster')        # Robot goes to Toaster
    PutObject(robot_list[0], 'Bread', 'Toaster') # Robot puts Bread in Toaster

def toast_bread(robot_list):
    # SubTask 2: Toast the slice of bread
    # Using robot1 to perform this task.
    SwitchOn(robot_list[0], 'Toaster')           # Robot switches on Toaster
    time.sleep(5)                                # Wait for a while to let the bread toast
    SwitchOff(robot_list[0], 'Toaster')          # Robot switches off Toaster

# Execute SubTask 1 with robot2
retrieve_bread_slice([robots[1]])

# Execute SubTask 2 with robot1
toast_bread([robots[0]])

# Task toast a slice of the bread loaf is done.
