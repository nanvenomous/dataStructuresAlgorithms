def decorator(input_fun):
	def mule_fun():
		print('pre function activity')
		input_fun()
		print('post function activity')
	return mule_fun

@decorator
def log(): print('doing a log')

log()
