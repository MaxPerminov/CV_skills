# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
for i in range(3):
    print(i)
else:
    print("yes")

print()

for j in range(6):
    print(j)
    if j == 3:
        break
else:
    print("No")
