```python
# TASK ALLOCATION

# Define the robots with their skills and mass capacities
robots = [
    {'name': 'robot1', 'skills': ['GoToObject', 'SliceObject', 'PickupObject'], 'mass': 100},
    {'name': 'robot2', 'skills': ['GoToObject', 'PickupObject', 'PutObject'], 'mass': 100},
    {'name': 'robot3', 'skills': ['GoToObject', 'BreakObject', 'ThrowObject'], 'mass': 100}
]

# Function to slice the apple using Robot 1
def slice_apple(robot):
    # 0: SubTask 1: Slice the Apple
    # 1: Go to the Knife using robot1.
    GoToObject(robot, 'Knife')
    # 2: Pick up the Knife using robot1.
    PickupObject(robot, 'Knife')
    # 3: Go to the Apple using robot1.
    GoToObject(robot, 'Apple')
    # 4: Slice the Apple using robot1.
    SliceObject('Apple')
    # 5: Go to the CounterTop using robot1.
    GoToObject(robot, 'CounterTop')
    # 6: Put the Knife back on the CounterTop using robot1.
    PutObject('Knife', 'CounterTop')

# Function to throw the sliced apple in trash using Robot 2
def throw_sliced_apple_in_trash(robot):
    # 0: SubTask 2: Throw the sliced Apple in the trash
    # 1: Go to the sliced Apple (assuming it's still recognized as "Apple") using robot2.
    GoToObject(robot, 'Apple')  
    # 2: Pick up the sliced Apple using robot2.
    PickupObject(robot, 'Apple')
    # 3: Go to the GarbageCan using robot2.
    GoToObject(robot, 'GarbageCan')
    # 4: Throw the sliced Apple in the GarbageCan using robot2.
    PutObject('Apple', 'GarbageCan')

# Execute SubTask 1 with Robot 1
slice_apple(robots[0])

# Execute SubTask 2 with Robot 2 after SubTask 1 is completed
throw_sliced_apple_in_trash(robots[1])

# Task Slice apple and throw it in trash is done
```

### Explanation of Code:
- **Robot Allocation**:
   - **Robot 1** is assigned to slice the apple because it has all necessary skills (`GoToObject`, `SliceObject`, `PickupObject`).
   - **Robot 2** is assigned to throw away the sliced apple because it has all necessary skills (`GoToObject`, `PickupObject`, `PutObject`).

- **Sequential Execution**:
   - The slicing of the apple must be completed before throwing it away. Therefore, we first call `slice_apple()` for Robot 1 and then call `throw_sliced_apple_in_trash()` for Robot 2.

This structure ensures that each subtask is handled by a capable robot while maintaining clarity and efficiency in task execution.