To accomplish the task of chilling the apple and washing the knife, we can break it down into two independent subtasks:

1. **Chill the Apple**: This involves putting the apple in the fridge.
2. **Wash the Knife**: This involves cleaning the knife in the sink.

### Skills Required for Each Subtask:
- **Chill the Apple**:
  - Skills Required: `GoToObject`, `PickupObject`, `OpenObject`, `PutObject`, `CloseObject`
  
- **Wash the Knife**:
  - Skills Required: `GoToObject`, `PickupObject`, `PutObject`, `SwitchOn`, `SwitchOff`

### Robot Capabilities:
Both robots have identical skills and mass capacity, which are sufficient to perform both subtasks.

### Mass of Objects:
- **Apple**: 0.2 kg
- **Knife**: 0.18 kg

Both robots have a mass capacity of 100 kg, which is more than sufficient for both objects.

### Task Allocation Analysis:
1. For **Chill the Apple**, any robot can perform this task since they possess all required skills.
2. For **Wash the Knife**, again, any robot can perform this task as they also possess all required skills.

Since both subtasks are independent and can be performed simultaneously, we will allocate one robot to each subtask to optimize efficiency.

### Robot Allocation Plan:
- Assign Robot 1 to chill the apple.
- Assign Robot 2 to wash the knife.

This allows both tasks to be executed in parallel without waiting for one another.

### Implementation Code:

```python
import time
import threading

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

# Create threads for parallel execution of subtasks
task1_thread = threading.Thread(target=chill_apple)
task2_thread = threading.Thread(target=wash_knife)

# Start executing both subtasks in parallel
task1_thread.start()
task2_thread.start()

# Wait for both threads to finish execution before concluding task completion
task1_thread.join()
task2_thread.join()

# Task completion message (optional)
print("Task of chilling apple and washing knife is done.")
```

### Conclusion:
The allocation plan ensures that both tasks are performed efficiently using two robots simultaneously while satisfying all constraints regarding skills and mass capacity.