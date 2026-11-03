def wash_lettuce(robot):
    # 0: SubTask 1: Wash the Lettuce
    # 1: Go to the Lettuce using robot.
    GoToObject(robot, 'Lettuce')
    # 2: Pick up the Lettuce using robot.
    PickupObject(robot, 'Lettuce')
    # 3: Go to the Sink using robot.
    GoToObject(robot, 'Sink')
    # 4: Put the Lettuce inside the sink using robot.
    PutObject(robot, 'Lettuce', 'Sink')
    # 5: Switch on the Faucet to clean the Lettuce using robot.
    SwitchOn(robot, 'Faucet')
    # 6: Wait for a while to let the lettuce clean.
    time.sleep(5)
    # 7: Switch off the Faucet using robot.
    SwitchOff(robot, 'Faucet')
    # 8: Pick up the clean Lettuce using robot.
    PickupObject(robot, 'Lettuce')

def place_lettuce_on_countertop(robot):
    # 0: SubTask 2: Place the Lettuce on Countertop
    # 1: Go to CounterTop using robot.
    GoToObject(robot, 'CounterTop')
    # 2: Put the Lettuce on CounterTop using robot.
    PutObject(robot, 'Lettuce', 'CounterTop')

# Execute SubTask 1 with Robot 1 (washes lettuce)
wash_lettuce(robots[0])

# Robot 1 puts washed lettuce on CounterTop
PutObject(robots[0], 'Lettuce', 'CounterTop')

# Robot 2 goes to CounterTop and picks up washed lettuce
GoToObject(robots[1], 'CounterTop')
PickupObject(robots[1], 'Lettuce')
