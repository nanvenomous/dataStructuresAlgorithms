class DecoratorExample:
	def __init__(self):
		""" Example Setup """
		self.name = 'Decorator_Example'

	@staticmethod
	def _private_static_method():
		print('I\'m a private static method!')
		print('Didn\'t need any attributes for this')
		print('Also only accessible within this class')
 
	@staticmethod
	def static_method():
		print('I\'m a static method!')
		print('Didn\'t need any attributes for this')
 
	def instance_method(self):
		print('I\'m an instance method!')
		print('I can access attributes for example, self.name is: ' + self.name)
		print('I can also call other class methods: ', self._private_static_method())

DecoratorExample.static_method()
print()

de = DecoratorExample()
de.instance_method()
print()