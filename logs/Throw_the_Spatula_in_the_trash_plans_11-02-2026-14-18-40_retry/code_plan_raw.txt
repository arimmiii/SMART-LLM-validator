```python
def throw_spatula_in_trash(robot_list):
    # robot_list = [robot2]
    # 0: SubTask 1: Throw the Spatula in the Trash
    # 1: Go to the Spatula using robot2.
    GoToObject(robot_list[0], 'Spatula')
    # 2: Pick up the Spatula using robot2.
    PickupObject(robot_list[0], 'Spatula')
    # 3: Go to the GarbageCan using robot2.
    GoToObject(robot_list[0], 'GarbageCan')
    # 4: Throw the Spatula in the GarbageCan using robot2.
    PutObject(robot_list[0], 'Spatula', 'GarbageCan')

# Execute SubTask 1 with Robot 2
throw_spatula_in_trash([robots[1]])

# Task throw the spatula in the trash is done
```

### Explanation of the Code:
1. **GoToObject(robot_list[0], 'Spatula')**: Robot 2 moves to the location of the spatula.
2. **PickupObject(robot_list[0], 'Spatula')**: Robot 2 picks up the spatula.
3. **GoToObject(robot_list[0], 'GarbageCan')**: Robot 2 moves to the trash can.
4. **PutObject(robot_list[0], 'Spatula', 'GarbageCan')**: Robot 2 throws the spatula into the trash can.

This sequence effectively completes the task of throwing the spatula in the trash, utilizing Robot 2's skills and mass capacity appropriately.