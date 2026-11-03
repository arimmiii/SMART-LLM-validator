def retrieve_bread_slice(robot_list):
    # robot_list = [robot2]
    # SubTask 1: Retrieve a slice of bread from the loaf
    # Go to the Bread loaf using robot2.
    GoToObject(robot_list[0], 'Bread')
    # Pick up a slice of Bread using robot2.
    PickupObject(robot_list[0], 'Bread')
    # Go to the Toaster using robot2.
    GoToObject(robot_list[0], 'Toaster')
    # Put the slice of Bread in the Toaster using robot2.
    PutObject(robot_list[0], 'Bread', 'Toaster')

def toast_bread(robot_list):
    # robot_list = [robot1]
    # SubTask 2: Toast the slice of bread
    # Switch on the Toaster using robot1.
    SwitchOn(robot_list[0], 'Toaster')
    # Wait for a while to let the bread toast.
    time.sleep(5)  
    # Switch off the Toaster using robot1.
    SwitchOff(robot_list[0], 'Toaster')
    
# Execute SubTask 1 with Robot 2
retrieve_bread_slice([robots[1]])

# Execute SubTask 2 with Robot 1
toast_bread([robots[0]])

# Task toast a slice of the bread loaf is done
