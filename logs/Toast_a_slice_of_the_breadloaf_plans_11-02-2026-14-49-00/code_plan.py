To toast a slice of bread, we can break down the task into several subtasks and allocate them to the appropriate robots based on their skills. Here’s how we can structure the code for this task:

### Task Description: Toast a slice of the bread loaf

### GENERAL TASK DECOMPOSITION
- **SubTask 1**: Retrieve a slice of bread from the loaf. (Skills Required: GoToObject, PickupObject, PutObject)
- **SubTask 2**: Toast the slice of bread. (Skills Required: GoToObject, PutObject, SwitchOn, SwitchOff)

### ROBOT CAPABILITIES
1. **Robot 1**:
   - Skills: ['GoToObject', 'SwitchOn', 'SwitchOff']
   - Mass Capacity: 100

2. **Robot 2**:
   - Skills: ['GoToObject', 'PickupObject', 'PutObject']
   - Mass Capacity: 100

3. **Robot 3**:
   - Skills: ['GoToObject', 'SliceObject', 'PickupObject']
   - Mass Capacity: 100

### OBJECTS
- Bread (mass = 0.699999988079071)
- Toaster (mass = 5.0)

### TASK ALLOCATION ANALYSIS
#### SubTask 1 Analysis:
- Required Skills for SubTask 1 are `GoToObject`, `PickupObject`, and `PutObject`.
- Robot capabilities:
    - Robot 2 has all required skills (`GoToObject`, `PickupObject`, `PutObject`).
  
#### SubTask 2 Analysis:
- Required Skills for SubTask 2 are `GoToObject`, `PutObject`, `SwitchOn`, and `SwitchOff`.
- Robot capabilities:
    - Robot 1 has all required skills (`GoToObject`, `SwitchOn`, and `SwitchOff`).

### SEQUENTIAL EXECUTION
The two subtasks will be executed sequentially because SubTask 2 depends on the completion of SubTask 1.

### CODE SOLUTION

```python
def retrieve_bread_slice(robot_list):
    # SubTask 1: Retrieve a slice of bread from the loaf
    # Using robot2 to perform this task.
    GoToObject(robot_list[0], 'Bread')          # Robot goes to Bread
    PickupObject(robot_list[0], 'Bread')        # Robot picks up Bread
    GoToObject(robot_list[0], 'Toaster')        # Robot goes to Toaster
    PutObject(robot_list[0], 'Bread', 'Toaster') # Robot puts Bread in Toaster

def toast_bread(robot_list):
    # SubTask 2: Toast the slice of bread
    # Using robot1 to perform this task.
    SwitchOn(robot_list[0], 'Toaster')           # Robot switches on Toaster
    time.sleep(5)                                # Wait for a while to let the bread toast
    SwitchOff(robot_list[0], 'Toaster')          # Robot switches off Toaster

# Execute SubTask 1 with robot2
retrieve_bread_slice([robots[1]])

# Execute SubTask 2 with robot1
toast_bread([robots[0]])

# Task toast a slice of the bread loaf is done.
```

### Explanation:
1. **SubTask 1** (`retrieve_bread_slice`): This function is executed by Robot 2, which retrieves a slice of bread from the loaf and places it in the toaster.
   
2. **SubTask 2** (`toast_bread`): This function is executed by Robot 1, which manages the toasting process by switching on the toaster, waiting for it to toast, and then switching it off.

This structure ensures that tasks are clearly defined and executed in order, allowing for efficient operation while utilizing each robot's strengths effectively.