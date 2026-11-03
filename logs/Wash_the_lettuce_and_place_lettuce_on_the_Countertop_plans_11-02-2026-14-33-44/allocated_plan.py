To allocate the tasks of washing the lettuce and placing it on the countertop, we need to analyze the required skills for each subtask and match them with the available robots' skills and mass capacities.

### Task Breakdown
1. **SubTask 1**: Wash the Lettuce
   - **Skills Required**: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff
   - **Mass of Lettuce**: 0.47 kg

2. **SubTask 2**: Place the Lettuce on the Countertop
   - **Skills Required**: GoToObject, PutObject
   - **Mass of Lettuce**: 0.47 kg

### Robot Analysis
- **Robot 1**
  - Skills: ['GoToObject', 'BreakObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject', ...]
  - Mass Capacity: 100 kg

- **Robot 2**
  - Skills: ['GoToObject', 'PickupObject', 'PutObject']
  - Mass Capacity: Not specified (assumed to be sufficient since it's not a limiting factor)

- **Robot 3**
  - Skills: ['GoToObject', 'BreakObject', 'SliceObject', 'SwitchOn', 'SwitchOff', ...]
  - Mass Capacity: 100 kg

### Task Allocation Decision
#### SubTask Allocation:
1. For **SubTask 1 (Wash the Lettuce)**:
   - Required skills are available in both Robot 1 and Robot 3.
   - Both robots can handle the mass of lettuce (0.47 kg).
   - We can assign this task to either Robot.

2. For **SubTask 2 (Place the Lettuce on Countertop)**:
   - Required skills are available in all three robots.
   - All robots can handle the mass of lettuce (0.47 kg).
   
### Execution Order:
The subtasks must be performed sequentially because SubTask 2 cannot start until SubTask 1 is completed.

### Final Allocation Plan:
- Assign SubTask 1 (Wash Lettuce) to Robot 1.
- After completing SubTask 1, assign SubTask 2 (Place Lettuce on Countertop) to Robot A or any robot that is free after completing their previous task.

### Implementation Code:

```python
def wash_lettuce(robot):
    # Execute washing process using robot's capabilities.
    robot.GoTo('Lettuce')
    robot.Pickup('Lettuce')
    robot.GoTo('Sink')
    robot.Put('Lettuce','Sink')
    robot.SwitchOn('Faucet')
    time.sleep(5) # Simulate washing time
    robot.SwitchOff('Faucet')
    robot.Pickup('Lettuce')

def place_lettuce_on_countertop(robot):
    # Execute placing process using robot's capabilities.
    robot.GoTo('CounterTop')
    robot.Put('Lettuce','CounterTop')

# Allocate tasks based on availability and skill set.
robot_for_washing = robots[0] # Assigning Robot1 for washing task 
wash_lettuce(robot_for_washing)

robot_for_placing = robots[0] # Reusing same Robot for placing task 
place_lettuce_on_countertop(robot_for_placing)

# Task wash lettuce and place it on countertop is done!
```

This allocation ensures that all constraints regarding skills and mass capacity are satisfied while performing tasks sequentially as required by their dependencies.