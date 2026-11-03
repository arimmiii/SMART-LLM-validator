To allocate the tasks of toasting a slice of bread, we need to analyze the subtasks, required skills, and the capabilities of the available robots.

### Task Description: Toast a slice of the bread loaf

### GENERAL TASK DECOMPOSITION
- **SubTask 1**: Retrieve a slice of bread from the loaf. (Skills Required: GoToObject, PickupObject, PutObject)
- **SubTask 2**: Toast the slice of bread. (Skills Required: GoToObject, PutObject, SwitchOn)

### ROBOT CAPABILITIES
1. **Robot 1**:
   - Skills: ['GoToObject', 'SwitchOn', 'SwitchOff']
   - Mass Capacity: 100

2. **Robot 2**:
   - Skills: ['GoToObject', 'PickupObject', 'PutObject']
   - Mass Capacity: 100

3. **Robot 3**:
   - Skills: ['GoToObject', 'SliceObject', 'PickupObject']
   - Mass Capacity: 100

### OBJECTS
- Bread (mass = 0.699999988079071)
- Toaster (mass = 5.0)

### ANALYSIS OF SUBTASKS AND ROBOT ALLOCATION
#### SubTask 1: Retrieve a slice of bread from the loaf.
- Required Skills:
    - GoToObject
    - PickupObject
    - PutObject
  
No single robot has all three skills required for this subtask; however:
- Robot 2 has `GoToObject`, `PickupObject`, and `PutObject` skills.

#### SubTask 2: Toast the slice of bread.
- Required Skills:
    - GoToObject
    - PutObject
    - SwitchOn
  
No single robot has all three skills required for this subtask; however:
- Robot 1 has `GoToObject` and `SwitchOn` skills but lacks `PutObject`.
  
Since Robot 2 can handle SubTask 1 completely and Robot 1 can handle part of SubTask 2 but lacks one skill (`Put Object`), we need to form teams or assign tasks accordingly.

### TEAM FORMATION FOR SUBTASKS
For SubTask 1:
- Assign Robot **2** to retrieve a slice of bread since it possesses all necessary skills.

For SubTask 2:
We can have both robots work together as follows:
- Assign Robot **1** to switch on the toaster after retrieving.
  
However, since there is no robot that can perform both subtasks independently due to skill gaps in individual robots:

#### Final Allocation Plan 
1. Execute SubTask **Retrieve Bread Slice** with Robot **2**
   
```python
def retrieve_bread_slice():
    # Steps for retrieving a slice from Bread Loaf using Robot #2's capabilities.
    GoTo('Bread')
    Pickup('Bread')
    GoTo('Toaster')
    Put('Bread', 'Toaster')

# Execute with Robot #2 
retrieve_bread_slice()
```

After completing this task:

2. Execute SubTask **Toast Bread Slice** with Robot **1**

```python
def toast_bread():
    # Steps for toasting using Robot #1's capabilities.
    GoTo('Toaster') 
    SwitchOn('Toaster')
    
# Execute with Robot #1 
toast_bread()
```

### CONCLUSION ON SEQUENCING AND PARALLELISM 
The two subtasks must be performed sequentially because they depend on each other; specifically, you cannot toast until you have retrieved and placed the bread in the toaster first.

Thus, we conclude that:

- The first subtask will be executed by *Robot #2*.
- The second subtask will be executed by *Robot #1* after completion of *Subtask #1*.

This allocation ensures that each robot is utilized effectively based on their skill sets while adhering to mass capacity constraints as well as task dependencies.