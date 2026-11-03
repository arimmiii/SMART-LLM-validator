```python
def wash_lettuce(robot_list):
    # robot_list = [robot1] or [robot3]
    # 0: SubTask 1: Wash the Lettuce
    # 1: Go to the Lettuce using the selected robot.
    GoToObject(robot_list[0], 'Lettuce')
    # 2: Pick up the Lettuce using the selected robot.
    PickupObject(robot_list[0], 'Lettuce')
    # 3: Go to the Sink using the selected robot.
    GoToObject(robot_list[0], 'Sink')
    # 4: Put the Lettuce inside the sink using the selected robot.
    PutObject(robot_list[0], 'Lettuce', 'Sink')
    # 5: Switch on the Faucet to clean the Lettuce using the selected robot.
    SwitchOn(robot_list[0], 'Faucet')
    # 6: Wait for a while to let the lettuce clean using the selected robot.
    time.sleep(5)
    # 7: Switch off the Faucet using the selected robot.
    SwitchOff(robot_list[0], 'Faucet')
    # 8: Pick up the clean Lettuce using the selected robot.
    PickupObject(robot_list[0], 'Lettuce')

def place_lettuce_on_countertop(robot_list):
    # robot_list = [robot2] or any other suitable robot
    # 0: SubTask 2: Place the Lettuce on Countertop
    # 1: Go to Countertop using the selected robot.
    GoToObject(robot_list[0], 'CounterTop')
    # 2: Put the Lettuce on Countertop using the selected robot.
    PutObject(robot_list[0], 'Lettuce', 'CounterTop')

# TASK ALLOCATION
robots = [
    {'name': 'robot1', 
     'skills': ['GoToObject', 'BreakObject', 'SwitchOn', 'SwitchOff', 
                'PickupObject', 'PutObject'], 
     'mass_capacity': 100},
    
    {'name': 'robot2', 
     'skills': ['GoToObject', 'PickupObject', 'PutObject'], 
     'mass_capacity': 100}, 
    
    {'name': 'robot3', 
     'skills': ['GoToObject', 'BreakObject', 'SliceObject', 
                'SwitchOn', 'SwitchOff', 
                'PickupObject', 'PutObject'], 
     'mass_capacity': 100}
]

# Execute SubTask 1 with Robot 1 or Robot 3
wash_lettuce([robots[0]])   # Using Robot 1 for washing

# Execute SubTask 2 with Robot 2
place_lettuce_on_countertop([robots[1]])   # Using Robot 2 for placing

# Task wash lettuce and place it on countertop is done
```

### Explanation:
- **wash_lettuce()** function is designed to handle washing tasks. It can be executed by either Robot 1 or Robot 3, both of which have sufficient skills for this task. The function includes all necessary steps from going to get lettuce, washing it, and picking it back up after cleaning.

- **place_lettuce_on_countertop()** function is responsible for placing washed lettuce onto a countertop. This task can be efficiently handled by Robot 2, which has all required skills.

### Execution:
- The functions are executed sequentially, ensuring that washing must be completed before placing it on a countertop. This structure allows for clear task allocation based on available skills and ensures that each subtask is performed effectively by suitable robots.