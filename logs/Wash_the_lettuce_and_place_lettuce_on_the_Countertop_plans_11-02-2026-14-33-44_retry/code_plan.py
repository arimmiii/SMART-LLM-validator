def wash_lettuce(robot):
    print(f"{robot['name']} is going to the Lettuce.")
    GoToObject(robot, 'Lettuce')
    
    print(f"{robot['name']} is picking up the Lettuce.")
    PickupObject(robot, 'Lettuce')
    
    print(f"{robot['name']} is going to the Sink.")
    GoToObject(robot, 'Sink')
    
    print(f"{robot['name']} is putting the Lettuce in the Sink.")
    PutObject(robot, 'Lettuce', 'Sink')
    
    print(f"{robot['name']} is switching on the Faucet.")
    SwitchOn(robot, 'Faucet')
    
    time.sleep(5)  # Simulate washing time
    
    print(f"{robot['name']} is switching off the Faucet.")
    SwitchOff(robot, 'Faucet')
    
    print(f"{robot['name']} is picking up the clean Lettuce.")
    PickupObject(robot, 'Lettuce')

def place_lettuce_on_countertop(robot):
    print(f"{robot['name']} is going to the CounterTop.")
    GoToObject(robot, 'CounterTop')
    
    print(f"{robot['name']} is placing the Lettuce on the CounterTop.")
    PutObject(robot, 'Lettuce', 'CounterTop')

# Allocate tasks based on availability and skill set.
robot_for_washing = robots[0]  # Assigning Robot1 for washing task 
wash_lettuce(robot_for_washing)

# After washing, assign SubTask 2 (Place Lettuce on Countertop) to Robot1 again
place_lettuce_on_countertop(robot_for_washing)

print("Task wash lettuce and place it on countertop is done!")
