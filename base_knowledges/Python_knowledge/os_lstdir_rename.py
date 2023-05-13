import os


path = r"C:\Users\test"  # check path to contain files' folder

files = os.listdir(path) 
for i in files:
    print(i)

for i in files:
    old_name = path + "\\" + i
    new_name = path + "\\adding_test_text" + i
    # new_name = path + "\\" + i[16:]  # back-up to previous names
    os.rename(old_name, new_name)

files = os.listdir(path)
for i in files:
    print(i)