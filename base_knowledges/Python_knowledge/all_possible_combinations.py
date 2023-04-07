import itertools

a = [1, 2, 3]
print("number of possible combinations: ", len(list((itertools.permutations(a)))), "\n\n")

print("combinations: \n")
for i in itertools.permutations(a):
    print(i, end="\n")
