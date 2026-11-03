To accomplish the task of chilling the apple and washing the knife, we can break it down into two independent subtasks:

1. **Chill the Apple**: This involves putting the apple in the fridge.
2. **Wash the Knife**: This involves cleaning the knife in the sink.

Since these two tasks can be executed in parallel, we will create separate functions for each subtask and use threading to run them concurrently.

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
   - The `chill_apple` function handles picking up an apple from its location, going to a fridge, opening it, placing it inside, and closing it afterward.

- **Wash the Knife**:
   - The `wash_knife` function manages picking up a knife from its location, going to a sink, placing it inside for cleaning by switching on a faucet for a specified duration before switching it off again.

- Both tasks are executed in parallel using threading which allows efficient use of time. After both threads complete their execution using `join()`, we print that both tasks are done.

### Task Allocation Analysis:
- Both subtasks can be performed independently by any robot since they have all necessary skills required for each task.
- Each robot has sufficient mass capacity (100) compared to both objects involved (mass of apple = ~0.2 and mass of knife = ~0.18).
  
This approach ensures that both tasks are completed efficiently without unnecessary delays.