import threading
import time
from queue import Queue

q = Queue()

def thread_function(name, q):
	print('Thread:', name, 'starting')
	time.sleep(2)
	print('Thread:', name, 'finishing')
	q.put(3)



if __name__ == "__main__":
	res = None
	x = threading.Thread(target=thread_function, args=(1, q))
	print('Main: before running Thread')
	x.start()
	print('Main: wait for the thread to finish')
	x.join()
	res = q.get()
	print('received:', res)
	print('Main: done')