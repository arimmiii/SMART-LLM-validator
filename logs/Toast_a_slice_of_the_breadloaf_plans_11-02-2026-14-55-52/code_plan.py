Here's the complete code solution for the task of toasting a slice of bread, including the task allocation based on robot capabilities:

### Task Description: Toast a slice of the bread loaf

### GENERAL TASK DECOMPOSITION
- **SubTask 1**: Retrieve a slice of bread from the loaf. (Skills Required: GoToObject, PickupObject, PutObject)
- **SubTask 2**: Toast the slice of bread. (Skills Required: GoToObject, PutObject, SwitchOn)

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

### TASK ALLOCATION AND CODE SOLUTION

```python
def retrieve_bread_slice(robot):
    # SubTask 1: Retrieve a slice of bread from the loaf using Robot #2.
    # 1: Go to the Bread loaf.
    GoToObject(robot, 'Bread')
    # 2: Pick up a slice of Bread.
    PickupObject(robot, 'Bread')
    # 3: Go to the Toaster.
    GoToObject(robot, 'Toaster')
    # 4: Put the slice of Bread in the Toaster.
    PutObject(robot, 'Bread', 'Toaster')

def toast_bread(robot):
    # SubTask 2: Toast the slice of bread using Robot #1.
    # 1: Switch on the Toaster.
    SwitchOn(robot, 'Toaster')
    # 2: Wait for a while to let the bread toast.
    time.sleep(5)  # Adjust time as necessary for toasting
    # 3: Switch off the Toaster.
    SwitchOff(robot, 'Toaster')

# Execute SubTask 1 with Robot #2
retrieve_bread_slice(robots[1])

# Execute SubTask 2 with Robot #1
toast_bread(robots[0])

# Task toast a slice of the bread loaf is done
```

### Explanation:
1. **retrieve_bread_slice** function is designed to handle all steps required to retrieve a slice of bread and place it in the toaster using Robot #2's capabilities.
   
2. **toast_bread** function manages switching on and off the toaster after waiting for an appropriate amount of time for toasting using Robot #1.

### Conclusion:
This code effectively utilizes each robot's skills while ensuring that tasks are performed sequentially due to their dependencies. Robot #2 retrieves and places the bread in the toaster before Robot #1 switches it on and off for toasting. This approach maximizes efficiency and adheres to skill requirements and mass capacities.