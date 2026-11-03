def put_mug_in_coffee_machine(robot):
    # Execute SubTask for putting mug in coffee machine.
    GoToObject(robot, 'Mug')               # Move to Mug location.
    PickupObject(robot, 'Mug')             # Pick up the Mug.
    GoToObject(robot, 'CoffeeMachine')      # Move to Coffee Machine location.
    PutObject(robot, 'Mug', 'CoffeeMachine')# Place Mug inside Coffee Machine.

# Execute SubTask using Robot available
put_mug_in_coffee_machine(robots[0])

# Task put mug in coffee machine is done
