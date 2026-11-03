To allocate the tasks of washing the fork and putting it in the bowl, we can form a team for SubTask 1 and assign SubTask 2 to Robot 2. Here's how we can structure the code for this task allocation:

### Task Decomposition
1. **SubTask 1**: Wash the Fork
   - **Skills Required**: GoToObject, PickupObject, PutObject (to place it in sink), SwitchOn (to turn on faucet), SwitchOff (to turn off faucet)

2. **SubTask 2**: Put the Fork in the Bowl
   - **Skills Required**: GoToObject, PickupObject (to pick up cleaned fork), PutObject (to place it in bowl)

### Robot Analysis
- **Robot 1**:
  - Skills: GoToObject, SwitchOn, SwitchOff
  - Mass Capacity: 100 kg
  
- **Robot 2**:
  - Skills: GoToObject, PickupObject, PutObject
  - Mass Capacity: 100 kg
  
- **Robot 3**:
  - Skills: GoToObject, BreakObject, ThrowObject
  - Mass Capacity: 100 kg

### Team Formation for SubTask Allocation

Since neither Robot 1 nor Robot 2 can perform all actions required for washing the fork alone, we will form a team of Robot 1 and Robot 2 to complete SubTask 1.

### Code Implementation

```python
def wash_fork(robot_list):
    # robot_list = [robot1, robot2]
    # SubTask 1: Wash the Fork
    # Step-by-step execution using both robots.
    
    # Robot 1 goes to the Fork.
    GoToObject(robot_list[0], 'Fork')
    # Robot 2 picks up the Fork.
    PickupObject(robot_list[0], 'Fork')
    
    # Both robots go to the Sink.
    GoToObject(robot_list[0], 'Sink')
    
    # Robot 2 puts the Fork inside the sink.
    PutObject(robot_list[0], 'Fork', 'Sink')
    
    # Robot 1 switches on the Faucet to clean the Fork.
    SwitchOn(robot_list[0], 'Faucet')
    
    # Wait for a while to let the Fork clean.
    time.sleep(5)
    
    # Robot 1 switches off the Faucet.
    SwitchOff(robot_list[0], 'Faucet')
    
    # Robot 2 picks up the clean Fork from Sink.
    PickupObject(robot_list[0], 'Fork')

def put_fork_in_bowl():
    # SubTask 2: Put the Fork in Bowl
    # Step-by-step execution using robot2.
    
    # Robot goes to Bowl.
    GoToObject('Bowl')
    
    # Puts cleaned Fork in Bowl.
    PutObject('Fork', 'Bowl')

# Execute SubTask with team of robots for washing fork
wash_fork([robots[0], robots[1]])

# Execute SubTask for putting fork in bowl with robot2
put_fork_in_bowl()

# Task wash fork and put it in bowl is done
```

### Explanation of Code Implementation:
- **Washing the Fork**:
   - The team of `Robot 1` and `Robot 2` works together where `Robot 1` handles actions that require switching on/off while `Robot 2` handles picking up and placing objects.

- **Putting Fork in Bowl**:
   - After washing is complete, `Robot 2` takes over to go to the bowl and place the cleaned fork inside.

This structured approach ensures that tasks are executed efficiently by leveraging each robot's strengths while addressing skill gaps through teamwork.