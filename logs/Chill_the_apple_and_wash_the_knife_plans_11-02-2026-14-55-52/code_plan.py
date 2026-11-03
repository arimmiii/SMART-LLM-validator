Here's the complete code solution for the task of chilling the apple and washing the knife, incorporating task allocation based on robot capabilities:

```python
from skills import GoToObject, OpenObject, CloseObject, SwitchOn, SwitchOff, PickupObject, PutObject
import time
import threading

# Define functions for each subtask
def chill_apple(robot):
    # Chill Apple SubTask
    GoToObject(robot, 'Apple')
    PickupObject(robot, 'Apple')
    GoToObject(robot, 'Fridge')
    OpenObject(robot, 'Fridge')
    PutObject(robot, 'Apple', 'Fridge')
    CloseObject(robot, 'Fridge')

def wash_knife(robot):
    # Wash Knife SubTask
    GoToObject(robot, 'Knife')
    PickupObject(robot, 'Knife')
    GoToObject(robot, 'Sink')
    PutObject(robot, 'Knife', 'Sink') 
    SwitchOn(robot, 'Faucet') 
    time.sleep(5)  # Simulate washing time
    SwitchOff(robot, 'Faucet') 
    PickupObject(robot, 'Knife') 
    GoToObject(robot, 'CounterTop') 
    PutObject(robot, 'Knife', 'CounterTop')

# TASK ALLOCATION
robots = [
    {'name': 'robot1', 
     'skills': ['GoToObject', 'OpenObject', 'CloseObject', 
                'SwitchOn', 'SwitchOff', 
                'PickupObject', 'PutObject'], 
     'mass': 100},
    
    {'name': 'robot2', 
     'skills': ['GoToObject', 'OpenObject', 'CloseObject',
                'SwitchOn', 'SwitchOff',
                'PickupObject', 'PutObject'], 
     'mass': 100}
]

# Create threads for parallel execution of subtasks
task1_thread = threading.Thread(target=chill_apple, args=(robots[0]['name'],))
task2_thread = threading.Thread(target=wash_knife, args=(robots[1]['name'],))

# Start executing both subtasks in parallel
task1_thread.start()
task2_thread.start()

# Wait for both threads to finish execution before concluding task completion
task1_thread.join()
task2_thread.join()

# Task completion message (optional)
print("Task of chilling apple and washing knife is done.")
```

### Explanation:
- **Subtasks**: The `chill_apple` function handles the process of chilling the apple by picking it up and placing it in the fridge. The `wash_knife` function manages cleaning the knife by placing it in the sink and turning on the faucet.
- **Robot Allocation**: Each robot is assigned to one subtask based on their skills. Both robots have sufficient skills to perform their respective tasks.
- **Parallel Execution**: The tasks are executed concurrently using threads to optimize efficiency.
- **Completion Message**: After both tasks are completed successfully (indicated by joining threads), a message is printed to confirm that the overall task is done.

This implementation ensures that both tasks are performed efficiently while adhering to all constraints regarding skills and mass capacity.