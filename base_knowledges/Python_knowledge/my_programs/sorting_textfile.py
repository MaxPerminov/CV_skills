# This textfile sorting program sorts text file's lines.
file_list = []
file_to_sort = open("file.txt", "r")
with file_to_sort:
    line = file_to_sort.readline()
    while line:
        file_list.append(line.capitalize())
        line = file_to_sort.readline()
file_list.sort()
file_to_write = open("file.txt", "w")
with file_to_write:
    file_to_write.writelines(file_list)
