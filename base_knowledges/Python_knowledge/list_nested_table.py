table1 = [[111, 112, 113], [221, 222, 223]]
print(table1[0][0])
print(table1[0][1])
print(table1[0][2])
print(table1[1][0])
print(table1[1][1])
print(table1[1][2])

print()

table1 = [[111, 112, 113], [221, 222, 223]]
for i in range(len(table1)):  # 2
    for j in range(len(table1[i])):  # 3
        print(table1[i][j])
