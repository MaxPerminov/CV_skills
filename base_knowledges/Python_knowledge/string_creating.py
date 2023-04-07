lst = [1, 2, 3, "a", "b", "c"]
a = ""
for i in range(6):
    a += str(lst[i])
print(a)


a = ["milk", "cheese", "eggs"]
b = ""
for i in a:
    if i == a[-1]:
        b += i
        continue
    else:
        b += i + " , "
print(b)
