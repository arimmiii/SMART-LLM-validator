Here's the complete code solution for washing the fork and putting it in the bowl, incorporating the task allocation strategy based on robot skills:

```python
import time
import threading

# Define the skills available for robots
def GoToObject(robot, object_name):
    print(f"{robot['name']} is going to {object_name}.")

def PickupObject(robot, object_name):
    print(f"{robot['name']} picked up {object_name}.")

def PutObject(robot, object_name, receptacle):
    print(f"{robot['name']} put {object_name} in {receptacle}.")

def SwitchOn(robot, object_name):
    print(f"{robot['name']} switched on {object_name}.")

def SwitchOff(robot, object_name):
    print(f"{robot['name']} switched off {object_name}.")

# Define robots with their skills and mass capacities
robots = [
    {'name': 'robot1', 'skills': ['GoToObject', 'BreakObject', 'ThrowObject'], 'mass': 100},
    {'name': 'robot2', 'skills': ['GoToObject', 'SwitchOn', 'SwitchOff'], 'mass': 100},
    {'name': 'robot3', 'skills': ['GoToObject', 'PickupObject', 'PutObject'], 'mass': 100}
]

# Function to wash the fork using a team of Robot2 and Robot3
def wash_fork():
    # Team: Robot2 (controls faucet) and Robot3 (handles fork)
    
    # Step 1: Robot3 goes to Fork
    GoToObject(robots[2], 'Fork')
    
    # Step 2: Robot3 picks up Fork
    PickupObject(robots[2], 'Fork')
    
    # Step 3: Robot3 goes to Sink
    GoToObject(robots[2], 'Sink')
    
    # Step 4: Robot3 puts Fork in Sink
    PutObject(robots[2], 'Fork', 'Sink')
    
    # Step 5: Robot2 switches on Faucet
    SwitchOn(robots[1], 'Faucet')
    
    # Step 6: Wait for a while to let the Fork clean.
    time.sleep(5)
    
    # Step 7: Robot2 switches off Faucet
    SwitchOff(robots[1], 'Faucet')
    
    # Step 8: Robot3 picks up cleaned Fork from Sink
    PickupObject(robots[2], 'Fork')

# Function to put the fork in the bowl using only Robot3
def put_fork_in_bowl():
    # Step 1: Robot3 goes to Bowl
    GoToObject(robots[2], 'Bowl')
    
    # Step 2: Robot3 puts Fork in Bowl
    PutObject(robots[2], 'Fork', 'Bowl')

# Execute SubTask1 (Wash the Fork) using Team [Robot2 + Robot3]
wash_fork()

# Execute SubTask2 (Put the Fork in Bowl) using only Robot3 after washing is done.
put_fork_in_bowl()

print("Task of washing the fork and putting it in the bowl is done.")
```

### Explanation of Code:
- **Robot Definitions**: Three robots are defined with their respective skills and mass capacities.
- **Functions**:
   - `wash_fork()`: This function coordinates actions between `Robot2` and `Robot3` to wash the fork. `Robot3` handles picking up and placing down objects while `Robot2` manages switching on/off the faucet.
   - `put_fork_in_bowl()`: This function allows `Robot3` to place the washed fork into the bowl.
- **Execution**:
   - The task starts by executing `wash_fork()` followed by `put_fork_in_bowl()`, ensuring that all steps are completed sequentially.

This code effectively demonstrates how tasks can be allocated based on robot capabilities while ensuring that dependencies between tasks are respected.