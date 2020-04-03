class HappyNumberOptimize:
	def __init__(self, cur=None, next=None):
		self.cur = cur
		self.next = next
		self.history = []

	def add_squared_digits(self):
		self.next = 0
		while self.cur != 0:
			self.next += (self.cur % 10)**2
			self.cur = int(self.cur/10)

	def loop_repeats_once(self):
		for elem in self.history[:-1]:
			if elem == self.history[-1]:
				return True
		return False

	def isHappy(self, n: int) -> bool:
		self.cur = n
		self.history = []
		while self.cur != 1:
			self.history.append(self.cur)
			self.add_squared_digits()
			self.cur = self.next
			if self.loop_repeats_once(): return False
		return True

class HappyNumber:
	def __init__(self, cur=None, next=None):
		self.cur = cur
		self.next = next
		self.possible_repeat = False
		self.history = []
		self.i1 = 0
		self.i2 = 0
		self.repeat_index = None

	def add_squared_digits(self):
		self.next = 0
		while self.cur != 0:
			self.next += (self.cur % 10)**2
			self.cur = int(self.cur/10)

	def _still_repeating(self):
		return self.history[self.i1 + self.repeat_index] == self.history[self.i2 + self.repeat_index]

	def _fully_repeated(self):
		return self.i1 + self.repeat_index == self.i2

	def loop_repeats_once(self):
		if not self.possible_repeat:
			for (i, elem) in enumerate(self.history[:-1]):
				if elem == self.history[-1]:
					self.possible_repeat = True
					self.i1 = i
					self.i2 = len(self.history) - 1
					self.repeat_index = 1
		else: # possible repeat
			if self._still_repeating():
				if self._fully_repeated():
					return True
			else: self.possible_repeat = False
			self.repeat_index += 1
		return False

	def isHappy(self, n: int) -> bool:
		self.cur = n
		self.possible_repeat = False
		self.history = []
		self.i1 = 0
		self.i2 = 0
		while self.cur != 1:
			self.history.append(self.cur)
			self.add_squared_digits()
			self.cur = self.next
			if self.loop_repeats_once(): return False
		return True
