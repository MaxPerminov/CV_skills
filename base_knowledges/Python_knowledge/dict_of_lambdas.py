# Use a dictionary to store functions:
test_calc = {
	'sum': lambda x, y: x + y,
	'subtract': lambda x, y: x - y
}

print(test_calc['sum'](12, 6))
print(test_calc['subtract'](12, 6))
