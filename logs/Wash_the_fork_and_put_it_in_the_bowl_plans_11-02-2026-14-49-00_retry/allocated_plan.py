To allocate the tasks of washing the fork and putting it in the bowl, we need to analyze the subtasks, required skills, and robot capabilities.

### GENERAL TASK DECOMPOSITION
1. **SubTask 1**: Wash the Fork.
   - **Skills Required**: GoToObject, PickupObject, PutObject, SwitchOn (for faucet), SwitchOff (for faucet)
   - **Mass of Objects**: Fork (0.04 kg), Faucet (0 kg)

2. **SubTask 2**: Put the Fork in the Bowl.
   - **Skills Required**: GoToObject, PickupObject, PutObject
   - **Mass of Objects**: Fork (0.04 kg), Bowl (0.47 kg)

### ROBOT CAPABILITIES
- **Robot 1**:
  - Skills: GoToObject, SwitchOn, SwitchOff
  - Mass Capacity: 100 kg

- **Robot 2**:
  - Skills: GoToObject, PickupObject, PutObject
  - Mass Capacity: 100 kg

- **Robot 3**:
  - Skills: GoToObject, BreakObject, ThrowObject
  - Mass Capacity: 100 kg

### ANALYSIS OF SUBTASKS AND ROBOT ALLOCATION

#### SubTask Allocation:
1. For **SubTask 1 (Wash the Fork)**:
   - Required skills are `GoToObject`, `PickupObject`, `PutObject`, `SwitchOn`, and `SwitchOff`.
   - Robot capabilities:
     - Robot 1 has `GoToObject`, `SwitchOn`, and `SwitchOff` but lacks `PickupObject` and `PutObject`.
     - Robot 2 has all necessary skills (`GoToObject`, `PickupObject`, and `PutObject`) but lacks control over water flow (`SwitchOn`/`SwitchOff`).
     - Robot combinations do not cover all required skills for this subtask.