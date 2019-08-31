def _tabbed_print_decorator(function_to_decorate):
	return lambda *args, **kwargs: function_to_decorate('\t', *args, **kwargs)

@_tabbed_print_decorator
def t_print(*args, **kwargs): print(*args, **kwargs)

t_print('dance')