Here's the complete code solution for the task of chilling the apple and washing the knife, incorporating the task allocation strategy discussed:

```python
from skills import GoToObject, OpenObject, CloseObject, SwitchOn, SwitchOff, PickupObject, PutObject
import time
import threading

# Define functions for each subtask
def chill_apple():
    # Chill Apple SubTask
    GoToObject('Apple')  # Step 1: Go to the Apple.
    PickupObject('Apple')  # Step 2: Pick up the Apple.
    GoToObject('Fridge')  # Step 3: Go to the Fridge.
    OpenObject('Fridge')  # Step 4: Open the Fridge.
    PutObject('Apple', 'Fridge')  # Step 5: Put Apple in the Fridge.
    CloseObject('Fridge')  # Step 6: Close Fridge.

def wash_knife():
    # Wash Knife SubTask
    GoToObject('Knife')  # Step 1: Go to the Knife.
    PickupObject('Knife')  # Step 2: Pick up the Knife.
    GoToObject('Sink')  # Step 3: Go to the Sink.
    PutObject('Knife', 'Sink')  # Step 4: Put the Knife inside the sink.
    
    SwitchOn('Faucet')  # Step 5: Switch on the Faucet to clean the Knife.
    
    time.sleep(5)  # Simulate washing time (wait for a while).
    
    SwitchOff('Faucet')  # Step 7: Switch off the Faucet.
    
    PickupObject('Knife')  # Step 8: Pick up the clean Knife.
    
    GoToObject('CounterTop')  # Step 9: Go to CounterTop.
    
    PutObject('Knife', 'CounterTop')  # Step10: Place Knife on CounterTop.

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

### Explanation:
- **Chill Apple Function**:
   - This function handles all steps required to chill an apple by placing it in a fridge. It includes navigating to the apple, picking it up, going to the fridge, opening it, placing the apple inside, and closing it.

- **Wash Knife Function**:
   - This function manages all steps required to wash a knife. It involves navigating to pick up the knife, moving it to a sink, putting it in there, turning on water from a faucet for cleaning (simulated with `time.sleep`), turning off water after cleaning, picking up and returning it back to a countertop.

- **Threading**:
   - The two functions are executed in parallel using Python's `threading` module. Each subtask runs in its own thread allowing them to be performed simultaneously.

- **Completion Message**:
   - After both threads have completed their tasks (using `join()`), a message is printed indicating that both tasks are done.

This implementation efficiently utilizes robot capabilities by performing independent tasks concurrently.