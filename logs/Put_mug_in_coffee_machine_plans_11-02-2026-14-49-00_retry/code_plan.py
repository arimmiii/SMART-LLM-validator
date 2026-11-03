def put_mug_in_coffee_machine(robot):
    # SubTask: Put the mug in the coffee machine
    # Step-by-step actions:
    
    # 1: Go to the Mug.
    GoToObject(robot, 'Mug')
    
    # 2: Pick up the Mug.
    PickupObject(robot, 'Mug')
    
    # 3: Go to the Coffee Machine.
    GoToObject(robot, 'CoffeeMachine')
    
    # 4: Open the Coffee Machine.
    OpenObject(robot, 'CoffeeMachine')
    
    # 5: Put the Mug inside the Coffee Machine.
    PutObject(robot, 'Mug', 'CoffeeMachine')
    
    # 6: Close the Coffee Machine.
    CloseObject(robot, 'CoffeeMachine')

# Execute SubTask with robot1
put_mug_in_coffee_machine(robots[0])

# Task put mug in coffee machine is done
