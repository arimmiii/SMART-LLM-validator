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
- For SubTask 1 (Retrieve a slice of bread):
    - Required skills are `GoToObject`, `PickupObject`, and `PutObject`.
    - Only Robot 2 has both `PickupObject` and `PutObject` skills along with `GoToObject`. 
    - Therefore, Robot 2 will perform this subtask.

#### SubTask 2 Analysis:
- For SubTask 2 (Toast the slice of bread):
    - Required skills are `GoToObject`, `PutObject`, `SwitchOn`, and `SwitchOff`.
    - Robot 1 has both `SwitchOn` and `SwitchOff` skills along with `GoToObject`.
    - Therefore, Robot 1 will perform this subtask.

### CODE Solution

```python
def retrieve_bread_slice(robot_list):
    # robot_list = [robot2]
    # SubTask 1: Retrieve a slice of bread from the loaf
    # Go to the Bread loaf using robot2.
    GoToObject(robot_list[0], 'Bread')
    # Pick up a slice of Bread using robot2.
    PickupObject(robot_list[0], 'Bread')
    # Go to the Toaster using robot2.
    GoToObject(robot_list[0], 'Toaster')
    # Put the slice of Bread in the Toaster using robot2.
    PutObject(robot_list[0], 'Bread', 'Toaster')

def toast_bread(robot_list):
    # robot_list = [robot1]
    # SubTask 2: Toast the slice of bread
    # Switch on the Toaster using robot1.
    SwitchOn(robot_list[0], 'Toaster')
    # Wait for a while to let the bread toast.
    time.sleep(5)  
    # Switch off the Toaster using robot1.
    SwitchOff(robot_list[0], 'Toaster')
    
# Execute SubTask 1 with Robot 2
retrieve_bread_slice([robots[1]])

# Execute SubTask 2 with Robot 1
toast_bread([robots[0]])

# Task toast a slice of the bread loaf is done
```

### Explanation:
- The function **retrieve_bread_slice** is executed by Robot 2, which retrieves a slice of bread from its loaf and places it in the toaster.
- The function **toast_bread** is executed by Robot 1, which manages switching on and off the toaster while waiting for it to toast.

This structured approach ensures that each subtask is allocated to robots based on their capabilities, allowing for efficient task completion.