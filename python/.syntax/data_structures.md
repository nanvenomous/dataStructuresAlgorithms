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

* clear
```
dq.clear()
```

### Dictionary
```
from collections import defaultdict

d = dict() # {}
dd = defaultdict(lambda: return 0)
```

### Set
```
s1 = set([1, 2, 2])
s2 = set([2, 3])
print(s1, s2) (1, 2) (2, 3)
```

* union
```
unionSet = s1.union(s2) 
print(unionSet) (1, 2, 3)
```

* intersection
```
intersectSet = s1.intersection(s2)
print(intersectSet) (2)
```

* difference
```
diffSet12 = s1.difference(s2)
print(diffSet12) (1)
diffSet21 = s2.difference(s1)
print(diffSet21) (3)
```

* symmetric difference
```
symDiffSet = s1.symmetric_difference(s2)
print(symDiffSet) (1, 3)
```

* super/sub set
```
sup = set([1, 2, 3, 4])
sub = set([2, 3])
sub.issubset(sup) True
sup.issuperset(sub) True
```

> set.add(x) # to end

> set.remove(x)

> set.discard(x) # won't throw error if not in set

> set.pop() # from front

> set.clear()

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
