To allocate the tasks of toasting a slice of bread loaf, we need to analyze the subtasks, required skills, and the capabilities of the available robots.

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
    - Therefore, Robot 2 can perform this subtask.

#### SubTask 2 Analysis:
- For SubTask 2 (Toast the slice of bread):
    - Required skills are `GoToObject`, `PutObject`, `SwitchOn`, and `SwitchOff`.
    - Robot 1 has both `SwitchOn` and `SwitchOff` skills along with `GoToObject`.