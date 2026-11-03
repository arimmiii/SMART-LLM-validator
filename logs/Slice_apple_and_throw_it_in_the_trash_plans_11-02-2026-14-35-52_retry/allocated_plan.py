To allocate the tasks of slicing an apple and throwing it in the trash, we first need to analyze the subtasks, required skills, and mass capacities of the robots available.

### Task Decomposition
1. **SubTask 1**: Slice the Apple.
   - **Skills Required**: GoToObject, PickupObject, SliceObject, PutObject
   - **Mass of Objects Involved**: Knife (0.18 kg), Apple (0.2 kg)

2. **SubTask 2**: Throw the sliced Apple in the trash.
   - **Skills Required**: GoToObject, PickupObject, PutObject
   - **Mass of Objects Involved**: Sliced Apple (assumed to still be recognized as 'Apple', 0.2 kg), GarbageCan (0.7 kg)

### Robot Analysis
- **Robot 1**
  - Skills: GoToObject, SliceObject, PickupObject
  - Mass Capacity: 100 kg

- **Robot 2**
  - Skills: GoToObject, PickupObject, PutObject
  - Mass Capacity: 100 kg

- **Robot 3**
  - Skills: GoToObject, BreakObject, ThrowObject
  - Mass Capacity: 100 kg

### Skill Matching for Subtasks:
- For SubTask 1 (Slice the Apple):
    - Robot 1 has all necessary skills (GoToObject + Slice + Pickup).
    - Robot capacity is sufficient for both Knife and Apple.

- For SubTask 2 (Throw the sliced Apple in Trash):
    - Robot 2 has all necessary skills (GoTo + Pickup + Put).
    - Robot capacity is sufficient for both Sliced Apple and GarbageCan.

### Task Execution Order:
The subtasks must be performed sequentially because SubTask 2 depends on completing SubTask 1 first.

### Task Allocation:
- Assign **SubTask 1** to Robot **1**.
- Assign **SubTask 2** to Robot **2**.

Both robots have sufficient mass capacity and possess all required skills for their respective tasks.

### Implementation Code:

```python
def slice_apple():
    # Subtask to slice an apple by robot1
    # Step-by-step actions performed by robot1 
    GoToObject('Knife')          # Move to Knife location
    PickupObject('Knife')        # Pick up Knife 
    GoToObject('Apple')          # Move to Apple location 
    SliceObject('Apple')         # Slice the apple 
    GoToObject('CounterTop')     # Return knife back to CounterTop 
    PutObject('Knife', 'CounterTop')

def throw_sliced_apple_in_trash():
    # Subtask to throw sliced apple by robot2 
    # Step-by-step actions performed by robot2 
    GoToObject('Apple')          # Move to sliced apple location  
    PickupObject('Apple')        # Pick up sliced apple  
    GoToObject('GarbageCan')     # Move towards Garbage Can  
    PutObject('Apple', 'GarbageCan')   # Dispose of sliced apple 

# Execute tasks sequentially as per allocation:
slice_apple()                     # Execute slicing task with robot1
throw_sliced_apple_in_trash()     # Execute throwing task with robot2

# Task "Slice an apple and throw it in trash" is done.
```

This solution ensures that each subtask is executed correctly while adhering to skill requirements and mass capacities of each robot involved.