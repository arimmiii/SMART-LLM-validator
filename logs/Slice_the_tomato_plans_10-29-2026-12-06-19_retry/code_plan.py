def slice_tomato(robot_list):
    # robot_list = [robot1, robot2]
    
    # 0: SubTask 1: Get the Knife
    # 1: Go to the Knife using robot1.
    GoToObject(robot_list[0], 'Knife')
    # 2: Pick up the Knife using robot1.
    PickupObject(robot_list[0], 'Knife')
    
    # 0: SubTask 2: Put the Knife down
    # 3: Go to the CounterTop using robot1.
    GoToObject(robot_list[0], 'CounterTop')
    # 4: Put the Knife back on the CounterTop using robot1.
    PutObject(robot_list[0], 'Knife', 'CounterTop')

    # 0: SubTask 3: Get the Tomato
    # 5: Go to the Tomato using robot2.
    GoToObject(robot_list[1], 'Tomato')
    # 6: Pick up the Tomato using robot2.
    PickupObject(robot_list[1], 'Tomato')
    
    # 0: SubTask 4: Slice the Tomato
    # 7: Slice the Tomato using robot2.
    SliceObject(robot_list[1], 'Tomato')

# Execute the task to slice the tomato with robots
slice_tomato([robots[0], robots[1]])

# Task slice the tomato is done
