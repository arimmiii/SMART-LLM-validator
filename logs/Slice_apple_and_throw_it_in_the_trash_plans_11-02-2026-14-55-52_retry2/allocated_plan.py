To allocate the tasks of slicing an apple and throwing it in the trash, we first need to analyze the subtasks, required skills, and robot capabilities.

### Task Decomposition
1. **SubTask 1**: Slice the Apple.
   - **Skills Required**: GoToObject, PickupObject, SliceObject, PutObject
   - **Mass of Objects**: Knife (0.18 kg), Apple (0.2 kg)
   
2. **SubTask 2**: Throw the sliced Apple in the trash.
   - **Skills Required**: GoToObject, PickupObject, PutObject
   - **Mass of Objects**: Sliced Apple (assumed to be still recognized as 'Apple', 0.2 kg), GarbageCan (0.7 kg)

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

#### SubTask Allocation:
1. For **SubTask 1 (Slice the Apple)**:
   - Required skills are available with Robot 1 (GoToObject, SliceObject) and Robot 2 (GoToObject).
   - However, Robot 1 has all necessary skills for this subtask.
   
2. For **SubTask 2 (Throw the sliced Apple in the trash)**:
   - Required skills are available with Robot 2 (GoToObject) and can also be performed by Robot 3 if needed.
   - Since both robots have sufficient capacity to handle a mass of up to approximately \(0.7 \text{kg}\) for GarbageCan.

### Execution Order:
The subtasks must be executed sequentially because SubTask 2 depends on completing SubTask 1 first.

### Final Allocation Plan:
- Assign **Robot 1** to perform SubTask *Slice the Apple*.
- Assign **Robot 2** to perform SubTask *Throw the sliced Apple in the trash* after Robot One completes its task.

### Implementation Code:

```python
def slice_apple():
    # Execute SubTask for slicing apple using Robot One's capabilities.
    # Step-by-step actions for slicing an apple...
    GoToObject('Knife')          # Move to Knife location
    PickupObject('Knife')        # Pick up Knife 
    GoToObject('Apple')          # Move to Apple location 
    Sliceobject('Apple')         # Perform slicing action 
    GoToobject('CounterTop')     # Return knife back 
    Putobject('Knife', 'CounterTop')

def throw_sliced_apple_in_trash():
    # Execute Subtask for throwing away sliced apple using Robot Two's capabilities.
    GoToobject('Apple')          # Move to Sliced apple location 
    Pickupobject('Apple')        # Pick up Sliced apple 
    Gotoobject('GarbageCan')     # Move towards Garbage Can 
    Putobject('Apple', 'GarbageCan') 

# Execute tasks sequentially based on allocation plan above

# Step by step execution of each subtask based on robot allocation plan:

slice_apple()                     # First execute slicing task with robot one

throw_sliced_apple_in_trash()     # Then execute throwing task with robot two

# Task is complete!
```

This approach ensures that all constraints regarding skill requirements and mass capacities are satisfied while maintaining a clear sequence of operations between subtasks.