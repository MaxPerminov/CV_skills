import os


path = r"C:\Users\test"  # check a path to contain items' folder

items = os.listdir(path) 
for i in items:
    print(i)

for i in items:
    old_name = path + "\\" + i
    new_name = path + "\\adding_test_text" + i
    # new_name = path + "\\" + i[16:]  # removes first 16 chars from item's name
    os.rename(old_name, new_name)

items = os.listdir(path)
for i in items:
    print(i)
