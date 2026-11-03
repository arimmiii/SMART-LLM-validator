To accomplish the task of chilling the apple and washing the knife, we can break it down into two independent subtasks:

1. **Chill the Apple**: This involves putting the apple in the fridge.
2. **Wash the Knife**: This involves cleaning the knife in the sink.

### Skills Required for Each Subtask:
- **Chill the Apple**:
  - Skills Required: `GoToObject`, `PickupObject`, `OpenObject`, `PutObject`, `CloseObject`
  
- **Wash the Knife**:
  - Skills Required: `GoToObject`, `PickupObject`, `PutObject`, `SwitchOn`, `SwitchOff`

### Robot Capabilities:
We have two robots available with identical skills and mass capacity:

- **Robot 1**:
  - Skills: All required skills for both subtasks
  - Mass Capacity: 100

- **Robot 2**:
  - Skills: All required skills for both subtasks
  - Mass Capacity: 100

### Object Details:
- **Apple** (mass = ~0.2)
- **Knife** (mass = ~0.18)

Both objects are well within each robot's mass capacity.

### Task Allocation Analysis:

1. For both subtasks, either robot can perform them since they possess all necessary skills.
2. Both tasks can be executed in parallel because they do not depend on each other.

### Robot Allocation Strategy:

Since both robots have identical capabilities, we can assign one robot to each subtask to maximize efficiency.

#### Proposed Allocation:
- Assign **Robot 1** to chill the apple.
- Assign **Robot 2** to wash the knife.

This way, both tasks will be performed simultaneously without any delays or dependencies between them.

### Implementation Code Example:

```python
import threading
import time

# Define functions for each subtask
def chill_apple():
    # Chill Apple SubTask
    GoToObject('Apple')
    PickupObject('Apple')
    GoToObject('Fridge')
    OpenObject('Fridge')
    PutObject('Apple', 'Fridge')
    CloseObject('Fridge')

def wash_knife():
    # Wash Knife SubTask
    GoToObject('Knife')
    PickupObject('Knife')
    GoToObject('Sink')
    PutObject('Knife', 'Sink') 
    SwitchOn('Faucet') 
    time.sleep(5) # Simulate washing time
    SwitchOff('Faucet') 
    PickupObject('Knife') 
    GoToObject('CounterTop') 
    PutObject('Knife', 'CounterTop')

# Create threads for parallel execution of tasks
task1_thread = threading.Thread(target=chill_apple)
task2_thread = threading.Thread(target=wash_knife)

# Start executing both subtasks in parallel
task1_thread.start()
task2_thread.start()

# Wait for both threads to finish execution before concluding task completion
task1_thread.join()
task2_thread.join()

print("Task of chilling apple and washing knife is done.")
```

### Conclusion:
The allocation strategy ensures that all constraints are satisfied while maximizing efficiency by performing tasks in parallel using two robots with matching capabilities.