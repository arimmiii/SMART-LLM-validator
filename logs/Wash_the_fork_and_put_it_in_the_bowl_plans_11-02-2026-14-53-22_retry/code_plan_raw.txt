To allocate the tasks of washing the fork and putting it in the bowl, we can break down the task into independent subtasks that can be executed sequentially. The subtasks will involve going to the fork, washing it, and then placing it in the bowl. Here's how we can structure the code for this task:

### Task Description: Wash the fork and put it in the bowl

### GENERAL TASK DECOMPOSITION
- **SubTask 1**: Wash the Fork. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)
- **SubTask 2**: Put the Fork in the Bowl. (Skills Required: GoToObject, PickupObject, PutObject)

### ROBOT CAPABILITIES
We have three robots with their respective skills:

1. **Robot 1**:
   - Skills: ['GoToObject', 'BreakObject', 'ThrowObject']
   - Mass Capacity: 100

2. **Robot 2**:
   - Skills: ['GoToObject', 'SwitchOn', 'SwitchOff']
   - Mass Capacity: 100

3. **Robot 3**:
   - Skills: ['GoToObject', 'PickupObject', 'PutObject']
   - Mass Capacity: 100

### ANALYSIS OF SUBTASKS
#### SubTask 1 (Wash the Fork):
- Required Skills:
    - GoToObject (available with all robots)
    - PickupObject (available only with Robot 3)
    - PutObject (available only with Robot 3)
    - SwitchOn (available only with Robot 2)
    - SwitchOff (available only with Robot 2)

Since no single robot has all required skills for this subtask, we need to form a team.

#### Team Formation for SubTask 1:
- Team of Robot 2 and Robot 3 can perform this task together.
    - Robot 2 will handle switching on/off the faucet.
    - Robot 3 will handle picking up and putting down objects.

#### SubTask 2 (Put the Fork in the Bowl):
- Required Skills:
    - GoToObject (available with all robots)
    - PickupObject (available only with Robot 3)
    - PutObject (available only with Robot 3)

For this subtask, only Robot 3 is needed since it has all required skills.

### CODE Solution  

```python
def wash_fork(robot_list):
    # robot_list = [robot2, robot3]
    
    # SubTask 1: Wash the Fork
    # Step 1: Go to the Fork using robot3.
    GoToObject(robot_list[1], 'Fork') # Robot 3 goes to Fork
    # Step 2: Pick up the Fork using robot3.
    PickupObject(robot_list[1], 'Fork')
    
    # Step 3: Go to Sink using robot3.
    GoToObject(robot_list[1], 'Sink')
    
    # Step 4: Put Fork inside Sink using robot3.
    PutObject(robot_list[1], 'Fork', 'Sink')
    
    # Step 5: Switch on Faucet using robot2.
    SwitchOn(robot_list[0], 'Faucet')
    
    # Step 6: Wait for a while to let Fork clean.
    time.sleep(5) 
    
    # Step 7: Switch off Faucet using robot2.
    SwitchOff(robot_list[0], 'Faucet')
    
    # Step 8: Pick up clean Fork using robot3.
    PickupObject(robot_list[1], 'Fork')

def put_fork_in_bowl(robot):
     # SubTask 2: Put Fork in Bowl
     # Step 1: Go to Bowl using robot3.
     GoToObject(robot, 'Bowl')
     # Step 2: Put Fork in Bowl using robot3.
     PutObject(robot, 'Fork', 'Bowl')

# Execute SubTask for washing fork with team of robots [robot2, robot3]
wash_fork([robots[1], robots[2]])

# Execute SubTask for putting fork in bowl with robot [robot3]
put_fork_in_bowl(robots[2])

# Task wash the fork and put it in bowl is done
```

### Explanation:
1. **wash_fork()** function handles washing of the fork by utilizing both `robot2` and `robot3`. 
   - `robot2` manages switching on/off water while `robot3` handles picking up and placing objects.

2. **put_fork_in_bowl()** function handles placing washed fork into a bowl by utilizing `robot3`.

This structure ensures that tasks are clear and organized while effectively utilizing each robot's capabilities based on their skills.