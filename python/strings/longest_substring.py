class Solution:
	def __init__(self):
		self.lengths = []

	def lengthOfLongestSubstring(self, s: str) -> int:
		self.populate_lengths(s)
		print(self.lengths)
		return max(self.lengths)

	def populate_lengths(self, s: str, n: int=1):
		if n >= len(s):
			self.lengths.append(len(s))
			return
		last = 0
		i = 0
		while i < len(s) - n:
			if (s[i] == s[i + n]):
				self.populate_lengths(s[last:i + n - 1], n + 1)
				last = i + n
				i += n
			else: i += 1
		self.populate_lengths(s[last:], n + 1)