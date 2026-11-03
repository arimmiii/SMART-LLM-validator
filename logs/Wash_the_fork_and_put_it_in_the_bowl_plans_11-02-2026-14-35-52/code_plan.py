Here's the complete code solution for the task of washing the fork and putting it in the bowl, including task allocation based on robot capabilities:

### Task Description: Wash the fork and put it in the bowl

### GENERAL TASK DECOMPOSITION
- **SubTask 1**: Wash the Fork. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)
- **SubTask 2**: Put the Fork in the Bowl. (Skills Required: GoToObject, PickupObject, PutObject)

### ROBOT CAPABILITIES
1. **Robot 1**:
   - Skills: ['GoToObject', 'SwitchOn', 'SwitchOff']
   - Mass Capacity: 100

2. **Robot 2**:
   - Skills: ['GoToObject', 'PickupObject', 'PutObject']
   - Mass Capacity: 100

3. **Robot 3**:
   - Skills: ['GoToObject', 'BreakObject', 'ThrowObject']
   - Mass Capacity: 100

### CODE SOLUTION

```python
import time
import threading

def wash_fork(robot_list):
    # Team of Robots [Robot_1 & Robot_2]
    # SubTask 1: Wash the Fork
    # Step-by-step execution as described above.
    
    # Robot 1 goes to fetch water from Faucet (`SwitchOn`).
    GoToObject(robot_list[0], 'Faucet')
    SwitchOn(robot_list[0], 'Faucet')
    
    # Robot 2 goes to pick up Fork.
    GoToObject(robot_list[1], 'Fork')
    PickupObject(robot_list[1], 'Fork')
    
    # Robot 2 puts Fork into Sink.
    GoToObject(robot_list[1], 'Sink')
    PutObject(robot_list[1], 'Fork', 'Sink')
    
    # Wait while water is running for cleaning.
    time.sleep(5)
    
    # Robot 2 picks up clean Fork again.
    PickupObject(robot_list[1], 'Fork')

def put_fork_in_bowl(robot):
    # SubTask 2: Put the Fork in the Bowl
    # Step-by-step execution as described above.
    
    GoToObject(robot, 'Bowl')
    PutObject(robot, 'Fork', 'Bowl')

# TASK ALLOCATION
robots = [
    {'name': 'robot1', 'skills': ['GoToObject', 'SwitchOn', 'SwitchOff'], 'mass': 100},
    {'name': 'robot2', 'skills': ['GoToObject', 'PickupObject', 'PutObject'], 'mass': 100},
]

# Execute SubTask A with Team of Robots [Robot_1 & Robot_2]
wash_fork([robots[0], robots[1]])

# Execute SubTask B with Robot B alone after completion of A.
put_fork_in_bowl(robots[1])

# Task wash the fork and put it in the bowl is done
```

### Explanation:
- The `wash_fork` function handles washing the fork using a team of Robot 1 and Robot 2. 
- The `put_fork_in_bowl` function handles putting the washed fork into the bowl using only Robot 2 since it has all necessary skills for that subtask.
- The tasks are executed sequentially to ensure that each step is completed before moving on to the next.

This structure ensures that all tasks are performed efficiently while adhering to skill requirements and robot capabilities.