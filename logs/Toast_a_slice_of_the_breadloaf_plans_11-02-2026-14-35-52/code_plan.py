Here's the complete code solution for the task of toasting a slice of bread, including the task allocation based on robot capabilities:

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

### SEQUENTIAL EXECUTION
The two subtasks will be executed sequentially because SubTask 2 depends on the completion of SubTask 1.

### CODE Solution

```python
def retrieve_bread_slice():
    # SubTask 1: Retrieve a slice of bread from the loaf
    # Go to Bread loaf.
    GoToObject('Bread')
    # Pick up a slice of Bread.
    PickupObject('Bread')
    # Go to Toaster.
    GoToObject('Toaster')
    # Put the slice in Toaster.
    PutObject('Bread', 'Toaster')

def toast_bread():
    # SubTask 2: Toast the slice of bread
    # Switch on Toaster.
    SwitchOn('Toaster')
    # Wait for it to toast.
    time.sleep(5)  
    # Switch off Toaster.
    SwitchOff('Toaster')

# Execute SubTask for Robot 2 (Retrieve Bread Slice)
retrieve_bread_slice()

# Execute SubTask for Robot 1 (Toast Bread)
toast_bread()

# Task toast a slice of the bread loaf is done
```

### Explanation:
1. **SubTask Execution**:
   - **Robot 2** retrieves a slice of bread from the loaf and places it in the toaster using its skills (`GoToObject`, `PickupObject`, and `PutObject`).
   - **Robot 1** then operates the toaster by switching it on, waiting for it to toast, and switching it off using its skills (`GoToObject`, `SwitchOn`, and `SwitchOff`).

This structure ensures that tasks are clearly defined and executed in sequence while effectively utilizing each robot's capabilities based on their skill sets.