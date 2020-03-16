def twice(function_to_decorate):
	def wrapper(*args, **kwargs):
		function_to_decorate(*args, **kwargs)
		function_to_decorate(*args, **kwargs)
	return wrapper

@twice
def what_i_did(thing): print('I did a ', thing)

what_i_did('dance')
what_i_did('jig')