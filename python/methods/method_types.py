def t_print(*args, **kwargs): print('\t', *args, **kwargs)

class DecoratorExample:
	def __init__(self):
		self.one = 1

	@staticmethod
	def _private_static_method():
		return 1
 
	@staticmethod
	def static_method_attempt_attribute_access():
		return self.one

	@staticmethod
	def static_method_attempt_other_method_access():
		return self.instance_method()
 
	def instance_method(self):
		return self._private_static_method() + self.one

	@classmethod
	def class_method(cls):
		return cls._private_static_method()

	@classmethod
	def class_method_calling_instance_method(cls):
		return cls.instance_method()

	@classmethod
	def class_method_attempt_attribute_access(cls):
		return cls.one