To allocate the tasks of washing the fork and putting it in the bowl, we first need to analyze the subtasks, required skills, and mass capacities of the robots available.

### Task Decomposition
1. **SubTask 1**: Wash the Fork
   - **Skills Required**: GoToObject, PickupObject, PutObject (to place it in sink), SwitchOn (to turn on faucet), SwitchOff (to turn off faucet)
   - **Mass of Objects**: Fork = 0.04 kg

2. **SubTask 2**: Put the Fork in the Bowl
   - **Skills Required**: GoToObject, PickupObject (to pick up cleaned fork), PutObject (to place it in bowl)
   - **Mass of Objects**: Bowl = 0.47 kg

### Robot Analysis
- **Robot 1**:
  - Skills: GoToObject, SwitchOn, SwitchOff
  - Mass Capacity: 100 kg
  
- **Robot 2**:
  - Skills: GoToObject, PickupObject, PutObject
  - Mass Capacity: 100 kg
  
- **Robot 3**:
  - Skills: GoToObject, BreakObject, ThrowObject
  - Mass Capacity: 100 kg

### Skill Matching for Subtasks
- For SubTask 1 (Wash the Fork):
    - Robot with skills needed is Robot 1 and Robot 2.
    - However, neither robot can perform all required actions alone since Robot 1 lacks `PickupObject` and `PutObject`, while Robot 2 lacks `SwitchOn` and `SwitchOff`.
    - Therefore a team is needed for this subtask.

- For SubTask 2 (Put the Fork in the Bowl):
    - This can be performed by Robot #2 as it has all necessary skills (`GoToObject`, `PickupObject`, `PutObject`).

### Team Formation for SubTask Allocation