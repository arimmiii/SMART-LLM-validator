To slice an apple and throw it in the trash, we can break down the task into a few subtasks. The subtasks can be executed sequentially since they depend on each other. Here’s how we can structure the code:

### Task Decomposition
- **SubTask 1**: Slice the Apple. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
- **SubTask 2**: Throw the sliced Apple in the trash. (Skills Required: GoToObject, PickupObject, PutObject)

### Code Implementation

```python
def slice_apple():
    # 0: SubTask 1: Slice the Apple
    # 1: Go to the Knife.
    GoToObject('Knife')
    # 2: Pick up the Knife.
    PickupObject('Knife')
    # 3: Go to the Apple.
    GoToObject('Apple')
    # 4: Slice the Apple.
    SliceObject('Apple')
    # 5: Go to the CounterTop.
    GoToObject('CounterTop')
    # 6: Put the Knife back on the CounterTop.
    PutObject('Knife', 'CounterTop')

def throw_sliced_apple_in_trash():
    # 0: SubTask 2: Throw the sliced Apple in the trash
    # 1: Go to the sliced Apple.
    GoToObject('Apple')  # Assuming the sliced apple is still recognized as 'Apple'
    # 2: Pick up the sliced Apple.
    PickupObject('Apple')
    # 3: Go to the Trash Can.
    GoToObject('GarbageCan')
    # 4: Throw the sliced Apple in the Trash Can.
    PutObject('Apple', 'GarbageCan')

# Execute SubTask 1
slice_apple()

# Execute SubTask 2
throw_sliced_apple_in_trash()

# Task Slice apple and throw it in the trash is done
```

### Explanation
1. **Slice the Apple**: The robot first goes to the knife, picks it up, then goes to the apple to slice it. After slicing, it puts the knife back on the countertop.
2. **Throw the Sliced Apple in the Trash**: The robot then goes to the sliced apple, picks it up, goes to the garbage can, and throws the sliced apple in the trash.

This code effectively completes the task of slicing an apple and disposing of it in the trash.