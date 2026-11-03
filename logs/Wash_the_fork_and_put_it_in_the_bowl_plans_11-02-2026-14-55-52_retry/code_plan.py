def wash_fork():
    # Team: Robot2 (controls faucet) and Robot3 (handles fork)
    
    # Step 1: Robot3 goes to Fork
    GoToObject(robots[2], 'Fork')
    
    # Step 2: Robot3 picks up Fork
    PickupObject(robots[2], 'Fork')
    
    # Step 3: Robot3 goes to Sink
    GoToObject(robots[2], 'Sink')
    
    # Step 4: Robot3 puts Fork in Sink
    PutObject(robots[2], 'Fork', 'Sink')
    
    # Step 5: Robot2 switches on Faucet
    SwitchOn(robots[1], 'Faucet')
    
    # Step 6: Wait for a while to let the Fork clean.
    time.sleep(5)
    
    # Step 7: Robot2 switches off Faucet
    SwitchOff(robots[1], 'Faucet')
    
    # Step 8: Robot3 picks up cleaned Fork from Sink
    PickupObject(robots[2], 'Fork')

def put_fork_in_bowl():
    # Step 1: Robot3 goes to Bowl
    GoToObject(robots[2], 'Bowl')
    
    # Step 2: Robot3 puts Fork in Bowl
    PutObject(robots[2], 'Fork', 'Bowl')

wash_fork()
put_fork_in_bowl()

print("Task of washing the fork and putting it in the bowl is done.")
