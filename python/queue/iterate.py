from queue import Queue

que = Queue()
que.put(1)
que.put(2)
que.put(3)

que.put(None)
for q in iter(que.get, None):
    print(q)
    que.put(q)

print()

que.put(None)
for q in iter(que.get, None):
    print(q)
    que.put(q)
