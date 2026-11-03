To allocate the tasks of putting Lettuce and Tomato in the fridge, we first need to analyze the subtasks, required skills, and mass capacities of the robots available.

### GENERAL TASK DECOMPOSITION
- **SubTask 1**: Put Lettuce in the fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
- **SubTask 2**: Put Tomato in the fridge. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)

### ROBOT CAPABILITIES
We have four robots with the following capabilities:

1. **Robot 1**:
   - Skills: ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'PickupObject', 'PutObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject']
   - Mass Capacity: 100

2. **Robot 2**:
   - Skills: ['GoToObject', 'SwitchOn', 'SwitchOff']
   - Mass Capacity: 100

3. **Robot 3**:
   - Skills: ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'PickupObject', 'PutObject','DropHand Object','Throw Object','Push Object','Pull Object']
   - Mass Capacity: 100

4. **Robot 4**:
   - Skills: ['GoToobject','Break Object','Throw Object']
   - Mass Capacity: 100

### OBJECTS AND THEIR MASSES
- Lettuce (mass = 0.4699999988079071)
- Tomato (mass = 0.11999998986721039)

### TASK ALLOCATION ANALYSIS
Both subtasks require a robot that can perform all necessary skills and handle the mass of each object.

#### SubTask Analysis:
1. **SubTask 1 (Put Lettuce in Fridge)**