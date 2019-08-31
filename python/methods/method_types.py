def t_print(*args, **kwargs): print('\t', *args, **kwargs)

class DecoratorExample:
	def __init__(self):
		""" Example Setup """
		self.name = 'Decorator_Example'

	@staticmethod
	def _private_static_method():
		t_print('I\'m a private static method!')
		t_print('Didn\'t need any attributes for this')
		t_print('Also only accessible within this class')
 
	@staticmethod
	def static_method():
		print('I\'m a static method!')
		print('Didn\'t need any attributes for this')
 
	def instance_method(self):
		print('I\'m an instance method!')
		print('I can access attributes for example, self.name is: ' + self.name)
		print('I can also call other class methods: ')
		self._private_static_method()

	@classmethod
	def class_method(cls):
		print('I\'m a class method!')
		print('I can only call other class methods: ')
		cls._private_static_method()

DecoratorExample.static_method()
print()

de = DecoratorExample()
de.instance_method()
print()

de.class_method()