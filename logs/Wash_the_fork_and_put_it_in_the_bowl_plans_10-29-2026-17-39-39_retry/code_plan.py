def wash_fork():
    # SubTask 1: Wash the Fork
    # Robot 1 goes to the Fork.
    GoToObject(robots[0], 'Fork')
    
    # Robot 1 picks up the Fork.
    PickupObject(robots[0], 'Fork')
    
    # Robot 1 goes to the Sink.
    GoToObject(robots[0], 'Sink')
    
    # Robot 1 puts the Fork inside the sink.
    PutObject(robots[0], 'Fork', 'Sink')
    
    # Robot 1 switches on the Faucet to clean the Fork.
    SwitchOn(robots[0], 'Faucet')
    
    # Wait for a while to let the Fork clean.
    time.sleep(5)
    
    # Robot 1 switches off the Faucet.
    SwitchOff(robots[0], 'Faucet')

def put_fork_in_bowl():
    # SubTask 2: Put the Fork in Bowl
    # Robot 2 goes to the Sink.
    GoToObject(robots[1], 'Sink')
    
    # Robot 2 picks up the cleaned Fork from Sink.
    PickupObject(robots[1], 'Fork')
    
    # Robot 2 goes to Bowl.
    GoToObject(robots[1], 'Bowl')
    
    # Robot 2 puts cleaned Fork in Bowl.
    PutObject(robots[1], 'Fork', 'Bowl')

# Execute SubTask with robot1 for washing fork
wash_fork()

# Execute SubTask for putting fork in bowl with robot2
put_fork_in_bowl()
