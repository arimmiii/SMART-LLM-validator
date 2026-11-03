To accomplish the task of chilling the apple and washing the knife, we can break it down into two independent subtasks:

1. **Chill the Apple**: This involves putting the apple in the fridge.
2. **Wash the Knife**: This involves cleaning the knife in the sink.

Since these two subtasks can be executed in parallel, we will create separate functions for each subtask and use threading to run them concurrently.

Here's how the code would look:

```python
import time
import threading

# Task Description: Chill the apple and wash the knife

# GENERAL TASK DECOMPOSITION
# Independent subtasks:
# SubTask 1: Chill the Apple. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
# SubTask 2: Wash the Knife. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)

def chill_apple():
    # 0: SubTask 1: Chill the Apple
    # 1: Go to the Apple.
    GoToObject('Apple')
    # 2: Pick up the Apple.
    PickupObject('Apple')
    # 3: Go to the Fridge.
    GoToObject('Fridge')
    # 4: Open the Fridge.
    OpenObject('Fridge')
    # 5: Put Apple in the Fridge
    PutObject('Apple', 'Fridge')
    # 6: Close Fridge
    CloseObject('Fridge')

def wash_knife():
    # 0: SubTask 2: Wash the Knife
    # 1: Go to the Knife.
    GoToObject('Knife')
    # 2: Pick up the Knife.
    PickupObject('Knife')
    # 3: Go to the Sink.
    GoToObject('Sink')
    # 4: Put the Knife inside the sink
    PutObject('Knife', 'Sink')
    # 5: Switch on the Faucet to clean the Knife
    SwitchOn('Faucet')
    # 6: Wait for a while to let knife clean.
    time.sleep(5)
    # 7: Switch off Faucet
    SwitchOff('Faucet')
    
# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=chill_apple)
task2_thread = threading.Thread(target=wash_knife)

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Task chill apple and wash knife is done

print("Chilling of apple and washing of knife is complete.")
```

### Explanation:
- **Chill the Apple**:
   - The function `chill_apple` handles picking up an apple from its location, going to a fridge, opening it, placing it inside, and closing it afterward.

- **Wash the Knife**:
   - The function `wash_knife` manages picking up a knife from its location, going to a sink, placing it inside for washing by turning on a faucet for a specified duration before turning it off.

- Both tasks are executed in parallel using threading which allows efficient use of time. After both threads complete their execution using `join()`, we print that both tasks are done.

### Task Allocation:
Given that both robots have identical skills required for each subtask (i.e., they can perform all necessary actions), you can assign either robot to either task without any issues. 

If you want to explicitly allocate tasks based on robots' capabilities:

```python
robots = [
   {'name': 'robot1', 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'PutObject'], 'mass':100},
   {'name': 'robot2', 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'SwitchOn', 'SwitchOff', 'PickupObject', 'Put Object'], 'mass':100}
]

# Assigning tasks based on skills (both robots have same skills)
robot_for_chill = robots[0]  
robot_for_wash = robots[1]  

# You could modify functions if needed to include robot references if required by your implementation context.
```

This setup ensures that both tasks are handled efficiently while utilizing available resources optimally.