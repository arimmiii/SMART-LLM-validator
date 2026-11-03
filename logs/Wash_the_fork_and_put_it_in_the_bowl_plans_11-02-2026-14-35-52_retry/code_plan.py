def wash_fork():
    # SubTask 1: Wash the Fork
    # Robot 1 will turn on the faucet and Robot 2 will handle the fork.
    
    # Robot 1 goes to fetch water from Faucet (`SwitchOn`).
    GoToObject(robots[0], 'Faucet')
    SwitchOn(robots[0], 'Faucet')
    
    # Robot 2 goes to pick up Fork.
    GoToObject(robots[1], 'Fork')
    PickupObject(robots[1], 'Fork')
    
    # Robot 2 puts Fork into Sink.
    GoToObject(robots[1], 'Sink')
    PutObject(robots[1], 'Fork', 'Sink')
    
    # Wait while water is running for cleaning.
    time.sleep(5)
    
def retrieve_fork():
    # Robot 2 picks up clean Fork again.
    GoToObject(robots[1], 'Sink')
    PickupObject(robots[1], 'Fork')

def put_fork_in_bowl():
    # SubTask 2: Put the Fork in the Bowl
    GoToObject(robots[1], 'Bowl')
    PutObject(robots[1], 'Fork', 'Bowl')

# Execute SubTask A
wash_fork()
retrieve_fork()

# Execute SubTask B
put_fork_in_bowl()
