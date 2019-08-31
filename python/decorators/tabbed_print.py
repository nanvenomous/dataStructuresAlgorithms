def _tabbed_print_decorator(function_to_decorate):
	def wrapper(*args, **kwargs):
		function_to_decorate('\t', *args, **kwargs)
	return wrapper

@_tabbed_print_decorator
def t_print(*args, **kwargs): print(*args, **kwargs)

t_print('dance')