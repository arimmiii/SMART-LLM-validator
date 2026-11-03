To effectively allocate the tasks of washing the fork and putting it in the bowl, we need to utilize a combination of robots that can collectively cover all required skills for each subtask. Here's how we can break down the task and allocate it accordingly:

### GENERAL TASK DECOMPOSITION
1. **SubTask 1**: Wash the Fork.
   - **Skills Required**: GoToObject, PickupObject, PutObject, SwitchOn (for faucet), SwitchOff (for faucet)

2. **SubTask 2**: Put the Fork in the Bowl.
   - **Skills Required**: GoToObject, PickupObject, PutObject

### ROBOT CAPABILITIES
- **Robot 1**:
  - Skills: GoToObject, SwitchOn, SwitchOff
  - Mass Capacity: 100 kg

- **Robot 2**:
  - Skills: GoToObject, PickupObject, PutObject
  - Mass Capacity: 100 kg

- **Robot 3**:
  - Skills: GoToObject, BreakObject, ThrowObject
  - Mass Capacity: 100 kg

### ANALYSIS OF SUBTASKS AND ROBOT ALLOCATION

#### SubTask Allocation:
1. For **SubTask 1 (Wash the Fork)**:
   - Required skills are `GoToObject`, `PickupObject`, `PutObject`, `SwitchOn`, and `SwitchOff`.
   - Robot capabilities:
     - Robot 1 can handle `GoToObject`, `SwitchOn`, and `SwitchOff`.
     - Robot 2 can handle `PickupObject` and `PutObject`.
   - Therefore, we can form a team of **Robot 1 and Robot 2** to wash the fork.

2. For **SubTask 2 (Put the Fork in the Bowl)**:
   - Required skills are `GoToObject`, `PickupObject`, and `PutObject`.
   - Robot capabilities:
     - Robot 2 has all necessary skills (`GoToObject`, `PickupObject`, and `PutObject`).
   - Therefore, we can assign **Robot 2** to put the fork in the bowl.

### CODE SOLUTION

```python
def wash_fork(robot_list):
    # robot_list = [robot1 (for faucet control), robot2 (for handling fork)]
    # SubTask: Wash the Fork
    # Step-by-step execution using both robots
    # Robot1 goes to Faucet to switch it on/off while Robot2 handles Fork
    
    # Robot1 goes to Sink to switch on Faucet
    GoToObject(robot_list[0], 'Sink')
    SwitchOn(robot_list[0], 'Faucet')
    
    # Robot2 goes to Fork
    GoToObject(robot_list[1], 'Fork')
    PickupObject(robot_list[1], 'Fork')
    
    # Both robots work together at Sink
    PutObject(robot_list[1], 'Fork', 'Sink') # Robot2 puts Fork in Sink
    
    time.sleep(5) # Wait for cleaning
    
    SwitchOff(robot_list[0], 'Faucet') # Robot1 switches off Faucet
    
def put_fork_in_bowl(robot):
    # SubTask: Put Fork in Bowl using robot2
    GoToObject(robot, 'Bowl')
    PutObject(robot, 'Fork', 'Bowl')

# Execute SubTask 1 with team of Robots [Robot1 (faucet control), Robot2 (fork handling)]
wash_fork([robots[0], robots[1]])

# Execute SubTask 2 with Robot2 alone
put_fork_in_bowl(robots[1])

# Task wash the fork and put it in the bowl is done.
```

### Explanation of Code Execution:
- In the function `wash_fork()`, both robots work together where Robot 1 manages faucet control while Robot 2 handles picking up and placing down the fork.
- After washing is complete, we call `put_fork_in_bowl()` where only Robot 2 is needed since it has all necessary skills for this subtask.

This approach ensures that all required skills are utilized efficiently while keeping tasks organized between multiple robots.