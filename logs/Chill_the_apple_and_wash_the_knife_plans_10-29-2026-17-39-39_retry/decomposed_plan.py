To accomplish the task of chilling the apple and washing the knife, we can break it down into two independent subtasks:

1. **Chill the Apple**: This involves putting the apple in the fridge.
2. **Wash the Knife**: This involves cleaning the knife in the sink.

Since these two subtasks can be executed in parallel, we will create separate functions for each subtask and use threading to run them concurrently.

Here's how the code would look:

```python
# Task Description: Chill the apple and wash the knife

# GENERAL TASK DECOMPOSITION
# Independent subtasks:
# SubTask 1: Chill the Apple. (Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject)
# SubTask 2: Wash the Knife. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)

# CODE
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
    # 6: Wait for a while to let the knife clean.
    time.sleep(5)
    # 7: Switch off the Faucet
    SwitchOff('Faucet')
    # 8: Pick up the clean Knife.
    PickupObject('Knife')
    # 9: Go to the CounterTop.
    GoToObject('CounterTop')
    # 10: Place the Knife on the CounterTop
    PutObject('Knife', 'CounterTop')

# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=chill_apple)
task2_thread = threading.Thread(target=wash_knife)

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Task chill the apple and wash the knife is done
```

### Explanation:
- **Chill the Apple**: The function `chill_apple` handles the process of picking up the apple, going to the fridge, and placing it inside.
- **Wash the Knife**: The function `wash_knife` manages the process of picking up the knife, washing it in the sink, and placing it back on the countertop.
- Both tasks are executed in parallel using threading, allowing for efficient use of time. After both threads complete, the task is considered done.