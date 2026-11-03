def wash_lettuce(robot):
    GoToObject(robot, 'Lettuce')
    PickupObject(robot, 'Lettuce')
    GoToObject(robot, 'Sink')
    PutObject(robot, 'Lettuce', 'Sink')
    SwitchOn(robot, 'Faucet')
    time.sleep(5)
    SwitchOff(robot, 'Faucet')
    PickupObject(robot, 'Lettuce')

def place_lettuce_on_countertop(robot):
    GoToObject(robot, 'CounterTop')
    PutObject(robot, 'Lettuce', 'CounterTop')

# Allocate tasks based on skills
selected_robot_for_washing = robots[0] if ('PickupObject' in robots[0]['skills'] and 
                                             all(skill in robots[0]['skills'] for skill in ['GoToObject', 
                                                                                          'PutObject',
                                                                                          'SwitchOn',
                                                                                          'SwitchOff'])) else robots[2]

wash_lettuce(selected_robot_for_washing)

selected_robot_for_placing = robots[0] if ('PutObject' in robots[0]['skills'] and 
                                             all(skill in robots[0]['skills'] for skill in ['GoToObject'])) else robots[1]

place_lettuce_on_countertop(selected_robot_for_placing)
