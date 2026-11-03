Here's the complete code solution for the task of putting Lettuce and Tomato in the fridge in parallel, including task allocation based on robot skills and mass capacity:

```python
from skills import GoToObject, OpenObject, CloseObject, PickupObject, PutObject
import threading

# Define the robots with their skills and mass capacities
robots = [
    {'name': 'robot1', 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'PickupObject', 'PutObject'], 'mass': 100},
    {'name': 'robot2', 'skills': ['GoToObject', 'SwitchOn', 'SwitchOff'], 'mass': 100},
    {'name': 'robot3', 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'PickupObject', 'PutObject'], 'mass': 100},
    {'name': 'robot4', 'skills': ['GoToObject', 'BreakObject', 'ThrowObject'], 'mass': 100}
]

# Define the functions for each subtask
def put_lettuce_in_fridge():
    # Steps for putting Lettuce in fridge
    GoToObject('Lettuce')
    PickupObject('Lettuce')
    GoToObject('Fridge')
    OpenObject('Fridge')
    PutObject('Lettuce', 'Fridge')
    CloseObject('Fridge')

def put_tomato_in_fridge():
    # Steps for putting Tomato in fridge
    GoToObject('Tomato')
    PickupObject('Tomato')
    GoToObject('Fridge')
    OpenObject('Fridge')
    PutObject('Tomato', 'Fridge')
    CloseObject('Fridge')

# Task Allocation:
# Assign Robot 1 to put Lettuce in the fridge (SubTask 1)
# Assign Robot 3 to put Tomato in the fridge (SubTask 2)

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
print("Task: Put Lettuce and Tomato in the fridge is done.")
```

### Explanation:
1. **Robot Definitions**: We define four robots with their respective skills and mass capacities. Robots 1 and 3 have all necessary skills to perform both subtasks.
  
2. **Function Definitions**: Two functions are defined to handle each subtask—`put_lettuce_in_fridge` and `put_tomato_in_fridge`.

3. **Threading**: We create two threads, one for each vegetable's task, allowing them to be executed concurrently.

4. **Execution**: Both threads are started simultaneously, and we wait for their completion using `join()`.

5. **Completion Message**: A message is printed once both tasks are completed.

This structure ensures that both vegetables are placed into the fridge efficiently without unnecessary delays.