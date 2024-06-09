def print_params(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    print()


list_ = [1, 'строка', True]
print_params(*list_)
list_ = []
print_params(*list_)
list_ = [1]
print_params(*list_)
list_ = ['строка', True]
print_params(*list_)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [58, 'voice', False]
values_dict = {'a': 69, 'b': 'number', 'c': 96}
print_params(*values_list, **values_dict)

values_list_2 = [63.9, False]
print_params(*values_list_2, 42)