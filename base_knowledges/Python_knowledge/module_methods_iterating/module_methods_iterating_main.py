from module_methods_iterating_module import Test, Test2


method_list = [method for method in dir(Test) if method.startswith('__') is False]
print(method_list)

for m in method_list:
    print(getattr(Test, m)(), end="")


print("\n")


# with different quantity of method parameters
def generate_params(dictionary, key):
    for i in dictionary[key]:
        yield i


def class_iterator(fn_params_generator, dictionary, module):
    for j in dictionary:
        getattr(module, j)(*fn_params_generator(dictionary, j))


getattr_data = {"fn_a": (1, 2), "fn_b": (3, 4, 5)}
class_iterator(generate_params, getattr_data, Test2)
