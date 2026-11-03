# CODE
def throw_spatula_in_trash():
    # 0: Throw the Spatula in the trash
    # 1: Go to the Spatula.
    GoToObject('Spatula')
    # 2: Pick up the Spatula.
    PickupObject('Spatula')
    # 3: Go to the GarbageCan.
    GoToObject('GarbageCan')
    # 4: Throw the Spatula in the GarbageCan.
    ThrowObject('Spatula')

# Execute the task to throw the Spatula in the trash
throw_spatula_in_trash()

# Task Throw the Spatula in the trash is done