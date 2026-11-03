def chill_apple(robot):
    GoToObject(robot, 'Apple')  # Step 1: Go to the Apple.
    PickupObject(robot, 'Apple')  # Step 2: Pick up the Apple.
    GoToObject(robot, 'Fridge')  # Step 3: Go to the Fridge.
    OpenObject(robot, 'Fridge')  # Step 4: Open the Fridge.
    PutObject(robot, 'Apple', 'Fridge')  # Step 5: Put Apple in the Fridge.
    CloseObject(robot, 'Fridge')  # Step 6: Close Fridge.

def wash_knife(robot):
    GoToObject(robot, 'Knife')  # Step 1: Go to the Knife.
    PickupObject(robot, 'Knife')  # Step 2: Pick up the Knife.
    GoToObject(robot, 'Sink')  # Step 3: Go to the Sink.
    PutObject(robot, 'Knife', 'Sink')  # Step 4: Put the Knife inside the sink.
    
    SwitchOn(robot, 'Faucet')  # Step 5: Switch on the Faucet to clean the Knife.
    
    time.sleep(5)  # Simulate washing time (wait for a while).
    
    SwitchOff(robot, 'Faucet')  # Step 7: Switch off the Faucet.
    
    PickupObject(robot, 'Knife')  # Step 8: Pick up the clean Knife.
    
    GoToObject(robot, 'CounterTop')  # Step 9: Go to CounterTop.
    
    PutObject(robot, 'Knife', 'CounterTop')  # Step10: Place Knife on CounterTop.

# Create threads for parallel execution of tasks
robot1 = {'name': 'robot1', 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 
                                        'SliceObject', 'SwitchOn', 'SwitchOff', 
                                        'PickupObject', 'PutObject', 
                                        'DropHandObject', 'ThrowObject', 
                                        'PushObject', 'PullObject']}

task1_thread = threading.Thread(target=chill_apple, args=(robot1,))
task2_thread = threading.Thread(target=wash_knife, args=(robot1,))

# Start executing both subtasks in parallel
task1_thread.start()
task2_thread.start()

# Wait for both threads to finish execution before concluding task completion
task1_thread.join()
task2_thread.join()

print("Task of chilling apple and washing knife is done.")
