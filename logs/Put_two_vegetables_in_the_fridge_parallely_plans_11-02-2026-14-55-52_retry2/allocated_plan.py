To allocate the tasks of putting Lettuce and Tomato in the fridge, we first need to analyze the subtasks, required skills, and mass capacities of the robots available.

### GENERAL TASK DECOMPOSITION
- **SubTask 1**: Put Lettuce in the fridge. 
  - **Skills Required**: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
  - **Mass of Object**: Lettuce (0.47 kg)
  
- **SubTask 2**: Put Tomato in the fridge.
  - **Skills Required**: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
  - **Mass of Object**: Tomato (0.12 kg)

### ROBOT ANALYSIS
We have four robots with the following skills and mass capacities:

1. **Robot 1**
   - Skills: ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'PickupObject', 'PutObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject']
   - Mass Capacity: 100 kg

2. **Robot 2**
   - Skills: ['GoToObject', 'SwitchOn', 'SwitchOff']
   - Mass Capacity: 100 kg

3. **Robot 3**
   - Skills: ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'PickupObject', 'PutObject','DropHand Object','Throw Object','Push Object','Pull Object']
   - Mass Capacity: 100 kg

4. **Robot 4**
   - Skills: ['GoToobject','Breakobject','Throwobject']
   - Mass Capacity: 100 kg

### TASK ALLOCATION BASED ON SKILLS AND MASS CAPACITY
Both subtasks require a robot that has all necessary skills to perform them:
- For both SubTask1 (Lettuce) and SubTask2 (Tomato), we need a robot with:
    * GoTo object skill
    * Pickup object skill
    * Open object skill
    * Put object skill
    * Close object skill
  
Only Robot 1 and Robot 3 possess all these required skills.

#### Allocation Strategy:
Since both subtasks can be performed independently without waiting for each other to complete (they are independent), we can execute them in parallel using two different robots.

### ASSIGNMENT OF ROBOTS TO SUBTASKS:
- Assign Robot 1 to SubTask1 (Put Lettuce in Fridge).
- Assign Robot 3 to SubTask2 (Put Tomato in Fridge).

Both robots have sufficient mass capacity to handle their respective objects since both objects weigh significantly less than their capacity.

### EXECUTION CODE STRUCTURE:

```python
import threading

def put_lettuce_in_fridge():
    # Steps for putting lettuce in fridge.
    GoTo('Lettuce')
    Pickup('Lettuce')
    GoTo('Fridge')
    Open('Fridge')
    Put('Lettuce','Fridge')
    Close('Fridge')

def put_tomato_in_fridge():
    # Steps for putting tomato in fridge.
    GoTo('Tomato')
    Pickup('Tomato')
    GoTo('Fridge')
    Open('Fridge')
    Put('Tomato','Fridge')
    Close('Fridge')

# Create threads for parallel execution of tasks.
task_lettuce_thread = threading.Thread(target=put_lettuce_in_fridge)
task_tomato_thread = threading.Thread(target=put_tomato_in_fridge)

# Start executing both subtasks concurrently.
task_lettuce_thread.start()
task_tomato_thread.start()

# Wait for both threads to finish execution.
task_lettuce_thread.join()
task_tomato_thread.join()

# Task completed successfully!
```

### Conclusion:
The task of putting Lettuce and Tomato into the fridge is efficiently allocated using two robots performing their respective subtasks concurrently due to their matching skills and sufficient mass capacity.