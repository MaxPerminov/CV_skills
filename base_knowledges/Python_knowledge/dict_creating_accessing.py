# dictionary from tuple:
a = ("Name", "Max"), ("Age", 39)
b = dict(a)   ##{'Name': 'Max', 'Age': 39}

# dict comprehension
test_Dict = {i: i for i in range(10)}  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

# creating dictionary through loop
user = {}
while True:
    if input("? ") == "y":
        a = input("key:")
        user[a] = input("value")
    else:
        break
print(user)
    

# Creating key of dictionary from several elements makes the type of this key tuple.
dict_key_tuple = {}
dict_key_tuple[1, 2, 3] = 3  # {(1, 2, 3): 3}


# accessing dictionary:

a = {'Name': 'Max', 'Age': 39}

for i in a:
    print(i)  # getting key
for i in a:
    print(a[i])  # getting keys value
