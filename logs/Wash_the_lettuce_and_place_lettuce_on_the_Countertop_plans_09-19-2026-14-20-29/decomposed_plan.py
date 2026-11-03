# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:
# SubTask 1: Wash the Lettuce. (Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff)
# SubTask 2: Place Lettuce on the Countertop. (Skills Required: GoToObject, PickupObject, PutObject)
# We can parallelize SubTask 1 and SubTask 2 because they don't depend on each other.

# CODE
def wash_lettuce():
    # 0: SubTask 1: Wash the Lettuce
    # 1: Go to the Lettuce.
    GoToObject('Lettuce')
    # 2: Pick up the Lettuce.
    PickupObject('Lettuce')
    # 3: Go to the Sink.
    GoToObject('Sink')
    # 4: Put the Lettuce in the Sink
    PutObject('Lettuce', 'Sink')
    # 5: Switch on the Faucet to clean the Lettuce
    SwitchOn('Faucet')
    # 6: Wait for a while to let the Lettuce clean.
    time.sleep(5)
    # 7: Switch off the Faucet
    SwitchOff('Faucet')

def place_lettuce_on_countertop():
    # 0: SubTask 2: Place Lettuce on the Countertop
    # 1: Go to the Lettuce.
    GoToObject('Lettuce')
    # 2: Pick up the Lettuce.
    PickupObject('Lettuce')
    # 3: Go to the Countertop.
    GoToObject('Countertop')
    # 4: Place the Lettuce on the Countertop.
    PutObject('Lettuce', 'Countertop')

# Parallelize SubTask 1 and SubTask 2
task1_thread = threading.Thread(target=wash_lettuce)
task2_thread = threading.Thread(target=place_lettuce_on_countertop)

# Start executing SubTask 1 and SubTask 2 in parallel
task1_thread.start()
task2_thread.start()

# Wait for both SubTask 1 and SubTask 2 to finish
task1_thread.join()
task2_thread.join()

# Task Wash the lettuce and place lettuce on the Countertop is done