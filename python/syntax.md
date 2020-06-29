# Data Structures

### Deque
```
from collections import deque
dq = deque([1, 2, 3])
```

* append
```
dq.append(4)
dq.appendleft(0)
```

* remove
```
dq.pop() # 4
dq.popleft() # 0
```

* extend
```
dq.extend([4, 5])
dq.extendleft([0, -1])
```

### Dictionary
```
from collections import defaultdict

d = dict() # {}
dd = defaultdict(lambda: return 0)
```

### List / Stack
```
l = list() # []
```

* copy
```
new_list = l.copy()
```

* insert
```
l.insert(0, val) # at beginning
l.append(val) # at end
```

* remove value from end
```
val = l.pop()
```

* reorder a list from indices
```
new_order = [3, 2, 0, 9..., n] # where n is nuber of indices in the list
l[:] = [l[i] for i in new_order]
```

### Queue
```
from queue import Queue
q = Queue()
```

* iterate over
```
q.put(None)
for qget in iter(q.get, None): pass
```

# Language

### Built-ins
* sorting
```
my_iterable.sort(reverse=True|False, key=_fun_returns_key)
```

### Statements

* conditional assignments
```
b = False
val = 0 if b else 1
print(val) # 1
```

### Variables

* value swap
```
val1, val2 = val2, val1
```

# Libraries

### numpy

* linspace
```
arr = np.linspace(0, end, end + 1) # increments of 1
arr = np.linspace(0, end, (end*2) + 1) # increments of 0.5
```

* slicing
```
new_arr = arr[1::2] # every second element of the array until the end starting at 1
```
