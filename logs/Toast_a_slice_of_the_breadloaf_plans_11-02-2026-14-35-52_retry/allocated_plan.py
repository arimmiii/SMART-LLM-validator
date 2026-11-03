To allocate the tasks of toasting a slice of bread, we need to analyze the subtasks, required skills, and the capabilities of the available robots. 

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
    - Robot 2 has all required skills.
  
#### SubTask 2 Analysis:
- Required Skills for SubTask 2 are `GoToObject`, `PutObject`, `SwitchOn`, and `SwitchOff`.
- Robot capabilities:
    - Robot 1 has all required skills.

### SEQUENTIAL OR PARALLEL EXECUTION
The two subtasks can be executed sequentially because SubTask 2 depends on the completion of SubTask 1; you cannot toast bread until it is retrieved and placed in the toaster.

### ROBOT ASSIGNMENT
Based on our analysis:

1. Assign **Robot 2** to perform **SubTask 1** (Retrieve a slice of bread).
   
```python
def retrieve_bread_slice():
    # Go to Bread loaf.
    GoToObject('Bread')
    # Pick up a slice of Bread.
    PickupObject('Bread')
    # Go to Toaster.
    GoToObject('Toaster')
    # Put the slice in Toaster.
    PutObject('Bread', 'Toaster')

# Execute SubTask for Robot 2
retrieve_bread_slice()
```

2. Assign **Robot 1** to perform **SubTask 2** (Toast the slice).
   
```python
def toast_bread():
    # Switch on Toaster.
    SwitchOn('Toaster')
    time.sleep(5) # Wait for it to toast.
    # Switch off Toaster.
    SwitchOff('Toaster')
    
# Execute SubTask for Robot 
toast_bread()
```

### FINAL ALLOCATION SUMMARY
- **Subtask Execution Order:** 
   - First execute Subtask by Robot **2**, then execute next subtask by Robot **1**
  
This allocation ensures that each robot is utilized effectively based on their skill sets while adhering to task dependencies and mass capacities.

Thus, we have successfully allocated tasks while ensuring that they are performed sequentially due to their dependency relationship!