a = "abcdefg"
for i in range(len(a)):
    print(a[i], end="")
    if i == len(a) - 1:
        break
    print(", ", end="")
