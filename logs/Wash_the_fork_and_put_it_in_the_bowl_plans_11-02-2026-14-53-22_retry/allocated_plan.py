To allocate the tasks of washing the fork and putting it in the bowl, we need to analyze the subtasks, required skills, and robot capabilities.

### Task Description: Wash the fork and put it in the bowl

### GENERAL TASK DECOMPOSITION
- **SubTask 1**: Wash the Fork. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)
- **SubTask 2**: Put the Fork in the Bowl. (Skills Required: GoToObject, PickupObject, PutObject)

### ROBOT CAPABILITIES
We have three robots with their respective skills:

1. **Robot 1**:
   - Skills: ['GoToObject', 'BreakObject', 'ThrowObject']
   - Mass Capacity: 100

2. **Robot 2**:
   - Skills: ['GoToObject', 'SwitchOn', 'SwitchOff']
   - Mass Capacity: 100

3. **Robot 3**:
   - Skills: ['GoToObject', 'PickupObject', 'PutObject']
   - Mass Capacity: 100

### ANALYSIS OF SUBTASKS
#### SubTask 1 (Wash the Fork):
- Required Skills:
    - GoToObject (available with all robots)
    - PickupObject (available only with Robot 3)
    - PutObject (available only with Robot 3)
    - SwitchOn (available only with Robot 2)
    - SwitchOff (available only with Robot 2)

Since no single robot has all required skills for this subtask, we need to form a team.

#### Team Formation for SubTask 1:
- Team of Robot 2 and Robot 3 can perform this task together.
    - Robot 2 will handle switching on/off the faucet.
    - Robot 3 will handle picking up and putting down objects.

#### SubTask 2 (Put the Fork in the Bowl):
- Required Skills:
    - Go