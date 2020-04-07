# Deque
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

# Dictionary
```
from collections import defaultdict

d = dict() # {}
dd = defaultdict(lambda: return 0)
```

# List / Stack
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

# Queue
```
from queue import Queue
q = Queue()
```

* iterate over
```
q.put(None)
for qget in iter(q.get, None): pass
```

# Statements

* conditional assignments
```
b = False
val = 0 if b else 1
print(val) # 1
```

# Variables

* value swap
```
val1, val2 = val2, val1
```
