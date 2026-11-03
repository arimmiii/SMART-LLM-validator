def put_mug_in_coffee_machine(robot):
    # Step-by-step execution of SubTask 1 using the specified robot
    # 0: SubTask 1: Put the mug in the coffee machine
    # 1: Go to the Mug using the robot.
    GoToObject(robot, 'Mug')
    # 2: Pick up the Mug using the robot.
    PickupObject(robot, 'Mug')
    # 3: Go to the Coffee Machine using the robot.
    GoToObject(robot, 'CoffeeMachine')
    # 4: Put the Mug in the Coffee Machine using the robot.
    PutObject(robot, 'Mug', 'CoffeeMachine')

# Execute SubTask 1 using Robot 1
put_mug_in_coffee_machine(robots[0])

# Task put mug in coffee machine is done
