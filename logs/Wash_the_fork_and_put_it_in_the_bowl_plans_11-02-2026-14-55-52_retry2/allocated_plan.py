To allocate the tasks of washing the fork and putting it in the bowl, we first need to analyze the subtasks, their required skills, and how they can be executed based on the available robots.

### GENERAL TASK DECOMPOSITION
1. **SubTask 1**: Wash the Fork.
   - **Skills Required**: GoToObject, PickupObject, PutObject, SwitchOn (for faucet), SwitchOff (for faucet)
   - **Mass of Objects**: Fork (0.04 kg), Faucet (0 kg)

2. **SubTask 2**: Put the Fork in the Bowl.
   - **Skills Required**: GoToObject, PickupObject, PutObject
   - **Mass of Objects**: Fork (0.04 kg), Bowl (0.47 kg)

### ROBOT ANALYSIS
We have three robots available:
- **Robot 1**
  - Skills: GoToObject, BreakObject, ThrowObject
  - Mass Capacity: 100 kg

- **Robot 2**
  - Skills: GoToObject, SwitchOn, SwitchOff
  - Mass Capacity: 100 kg

- **Robot 3**
  - Skills: GoToObject, PickupObject, PutObject
  - Mass Capacity: 100 kg

### SKILL AND MASS CAPACITY MATCHING
#### SubTask Allocation:
1. For SubTask 1 (Wash the Fork):
   - Required skills are `GoToObject`, `PickupObject`, `PutObject`, `SwitchOn`, and `SwitchOff`.
   - Robot capabilities:
     - Robot 1 lacks necessary skills for this task.
     - Robot 2 has `GoToObject`, `SwitchOn`, and `SwitchOff` but lacks `Pickup` and `Put`.
     - Robot 3 has `GoToObject`, `Pickup`, and `Put` but lacks control over water (`SwitchOn`/`SwitchOff`).
   
   Since no single robot can perform all required actions for washing the fork due to skill gaps:
   We will form a team consisting of:
   * Robot 2 for controlling water (`SwitchOn`/`SwitchOff`)
   * Robot 3 for picking up and putting down objects.

2. For SubTask 2 (Put the Fork in the Bowl):
   - Required skills are `GoToObject`, `PickupObject`, and `PutObject`.
   - This task can be performed by Robot 3 alone since it possesses all necessary skills.

### EXECUTION SEQUENCE AND ALLOCATION STRATEGY
Given that washing must occur before placing it in a bowl:

- Execute SubTask1 with Robots Team [Robot2 + Robot3].
- After completing SubTask1 successfully,
- Execute SubTask2 with Robot3.

### FINAL ALLOCATION PLAN

```python
# Execute SubTask1 using Team [Robot2 + Robot3]
def wash_fork():
    # Step-by-step execution as described earlier...
    # Team members will coordinate their actions accordingly.
    # Example coordination could involve:
    # Robot3 picks up fork -> moves to sink -> puts fork down -> 
    # while robot2 switches on faucet -> waits -> switches off faucet ->
    # then robot3 picks up cleaned fork again.

# Execute SubTask2 using only Robot3 after completion of wash_fork()
def put_fork_in_bowl():
    # Step-by-step execution as described earlier...
```

This ensures that both subtasks are completed efficiently while adhering to skill requirements and mass capacities without unnecessary delays or resource wastage.

In conclusion:
- The tasks must be performed sequentially due to dependencies between them.
- A combination of robots is used where necessary based on their skill sets to ensure successful completion of each subtask while maintaining efficiency through teamwork where needed.