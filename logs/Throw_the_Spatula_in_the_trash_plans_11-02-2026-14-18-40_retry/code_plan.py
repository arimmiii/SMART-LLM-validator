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
