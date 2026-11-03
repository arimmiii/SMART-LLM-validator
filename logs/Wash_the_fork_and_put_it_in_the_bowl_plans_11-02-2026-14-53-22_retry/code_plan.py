def wash_fork(robot_list):
    # robot_list = [robot2, robot3]
    
    # SubTask 1: Wash the Fork
    # Step 1: Go to the Fork using robot3.
    GoToObject(robot_list[1], 'Fork') # Robot 3 goes to Fork
    # Step 2: Pick up the Fork using robot3.
    PickupObject(robot_list[1], 'Fork')
    
    # Step 3: Go to Sink using robot3.
    GoToObject(robot_list[1], 'Sink')
    
    # Step 4: Put Fork inside Sink using robot3.
    PutObject(robot_list[1], 'Fork', 'Sink')
    
    # Step 5: Switch on Faucet using robot2.
    SwitchOn(robot_list[0], 'Faucet')
    
    # Step 6: Wait for a while to let Fork clean.
    time.sleep(5) 
    
    # Step 7: Switch off Faucet using robot2.
    SwitchOff(robot_list[0], 'Faucet')
    
    # Step 8: Pick up clean Fork using robot3.
    PickupObject(robot_list[1], 'Fork')

def put_fork_in_bowl(robot):
     # SubTask 2: Put Fork in Bowl
     # Step 1: Go to Bowl using robot3.
     GoToObject(robot, 'Bowl')
     # Step 2: Put Fork in Bowl using robot3.
     PutObject(robot, 'Fork', 'Bowl')

# Execute SubTask for washing fork with team of robots [robot2, robot3]
wash_fork([robots[1], robots[2]])

# Execute SubTask for putting fork in bowl with robot [robot3]
put_fork_in_bowl(robots[2])

# Task wash the fork and put it in bowl is done
