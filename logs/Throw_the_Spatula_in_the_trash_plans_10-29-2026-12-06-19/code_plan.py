```python
def throw_spatula_in_trash(robot_list):
    # robot_list = [robot1, robot2]
    # 0: SubTask 1: Throw the Spatula in the Trash
    # 1: Robot 2 goes to the Spatula.
    GoToObject(robot_list[1], 'Spatula')
    # 2: Robot 2 picks up the Spatula.
    PickupObject(robot_list[1], 'Spatula')
    # 3: Robot 2 goes to the Garbage Can.
    GoToObject(robot_list[1], 'GarbageCan')
    # 4: Robot 1 throws the Spatula in the Garbage Can.
    ThrowObject(robot_list[0], 'Spatula', 'GarbageCan')

# Execute SubTask with both robots
throw_spatula_in_trash([robots[0], robots[1]])

# Task throw the spatula in the trash is done
```

### Explanation:
1. **Robot Team**: We are using both robots to complete this task. Robot 2 will handle picking up and moving, while Robot 1 will handle throwing.
   
2. **Execution Steps**:
   - **Robot 2** moves to the spatula and picks it up.
   - **Robot 2** then moves to the garbage can.
   - Finally, **Robot 1** throws the spatula into the garbage can.

This approach effectively utilizes both robots' skills to complete the task of throwing the spatula in the trash.