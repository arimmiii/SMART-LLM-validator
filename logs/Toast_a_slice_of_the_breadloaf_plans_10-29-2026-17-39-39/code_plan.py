Here's how we can structure the code for the task of toasting a slice of bread, including the task allocation based on the robots' skills:

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
For SubTask 1 ("Retrieve a slice of bread from the loaf"):
- Required Skills are `GoToObject`, `PickupObject`, and `PutObject`.
- Robot capabilities:
    - Robot 2 has all required skills.

#### SubTask 2 Analysis:
For SubTask 2 ("Toast the slice of bread"):
- Required Skills are `GoToObject`, `PutObject`, `SwitchOn`, and `SwitchOff`.
- Robot capabilities:
    - Robot 1 has all required skills.

### CODE Solution  

```python
def retrieve_bread_slice(robot):
    # SubTask 1: Retrieve a slice of bread from the loaf
    # Go to the Bread loaf using robot.
    GoToObject(robot, 'Bread')
    # Pick up a slice of Bread using robot.
    PickupObject(robot, 'Bread')
    # Go to the Toaster using robot.
    GoToObject(robot, 'Toaster')
    # Put the slice of Bread in the Toaster using robot.
    PutObject(robot, 'Bread', 'Toaster')

def toast_bread(robot):
    # SubTask 2: Toast the slice of bread
    # Switch on the Toaster using robot.
    SwitchOn(robot, 'Toaster')
    # Wait for a while to let the bread toast.
    time.sleep(5)  # Adjust time as necessary for toasting
    # Switch off the Toaster using robot.
    SwitchOff(robot, 'Toaster')

# Execute SubTask 1 with Robot 2
retrieve_bread_slice(robots[1])

# Execute SubTask 2 with Robot 1
toast_bread(robots[0])

# Task toast a slice of the bread loaf is done
```

### Explanation:
1. **SubTask Execution**:
   - The function `retrieve_bread_slice` is executed by Robot 2 since it possesses all necessary skills to retrieve and place the bread in the toaster.
   - The function `toast_bread` is executed by Robot 1 since it has all necessary skills to operate the toaster.

This structure ensures that each subtask is allocated to an appropriate robot based on their skill set while maintaining clarity and efficiency in executing each part of the task sequentially.