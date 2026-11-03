To allocate the tasks of slicing an apple and throwing it in the trash, we need to analyze the subtasks, required skills, and robot capabilities.

### Task Decomposition
1. **SubTask 1**: Slice the Apple.
   - **Skills Required**: GoToObject, PickupObject, SliceObject, PutObject
   - **Mass of Objects Involved**: Knife (0.18 kg), Apple (0.2 kg)
   
2. **SubTask 2**: Throw the sliced Apple in the trash.
   - **Skills Required**: GoToObject, PickupObject, PutObject
   - **Mass of Objects Involved**: Sliced Apple (0.2 kg), GarbageCan (0.7 kg)

### Robot Capabilities
- **Robot 1**
  - Skills: GoToObject, SliceObject, PickupObject
  - Mass Capacity: 100 kg

- **Robot 2**
  - Skills: GoToObject, PickupObject, PutObject
  - Mass Capacity: 100 kg

- **Robot 3**
  - Skills: GoToObject, BreakObject, ThrowObject
  - Mass Capacity: 100 kg

### Analysis of Subtasks and Robot Allocation

#### SubTask 1 (Slice the Apple)
- Required skills are available with:
    * Robot 1 has all necessary skills to perform this task.
  
#### SubTask 2 (Throw the sliced Apple in the trash)
- Required skills are available with:
    * Robot 2 has all necessary skills to perform this task.

### Execution Order and Parallelism
The subtasks can be executed sequentially because:
- The second subtask depends on completing the first subtask since you need to slice the apple before throwing it away.

### Task Allocation Summary:
1. Assign Robot 1 to SubTask 1 (Slice the Apple).
2. After completion of SubTask 1 by Robot 1:
   Assign