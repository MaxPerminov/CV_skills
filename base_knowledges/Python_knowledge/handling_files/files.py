# getting unique lines from two files

# file1 = open("text1.txt")
# file2 = open("text2.txt")
# with file1, file2:
#     list1 = file1.readlines()
#     list2 = file2.readlines()
#     dif = [a for a in list1 + list2 if a not in list1 or a not in list2]
#     print("These lines do not match:", dif)

#######################################################################################
# Writing text file statistic:
# characters' number
# lines' number
# consonants' number
# vowels' number
# digits' number

# with open("text1.txt", "r") as file1, open("text2.txt", "w+") as file2:
#     char = (len(file1.read()))
#     file2.write("chars " + str(char) + "\n")
# with open("text1.txt", "r") as file1, open("text2.txt", "a+") as file2:
#     lines = file1.read().count("\n") + 1
#     file2.write("lines " + str(lines) + "\n")
# with open("text1.txt", "r") as file1, open("text2.txt", "a+") as file2:
#     vowels = file1.read()
#     v = 0
#     for i in vowels.lower():
#         if i == "a" or i == "e" or i == "i" or\
#            i == "o" or i == "u":
#             v += 1
#     file2.write("vowels " + str(v) + "\n")
# with open("text1.txt", "r") as file1, open("text2.txt", "a+") as file2:
#     consonant = file1.read()
#     c = 0
#     for y in consonant.lower():
#         if y == "b" or y == "c" or y == "d" or y == "f" or y == "g" or y == "j" or y == "k" or\
#            y == "l" or y == "m" or y == "n" or y == "p" or y == "q" or y == "s" or y == "t" or\
#            y == "v" or y == "x" or y == "z" or y == "h" or y == "r" or y == "w" or y == "y":
#             c += 1
#     file2.write("consonant " + str(c) + "\n")
# with open("text1.txt", "r") as file1, open("text2.txt", "a+") as file2:
#     nums = file1.read()
#     nu = 0
#     for n in nums:
#         if n == "0" or n == "1" or n == "2" or n == "3" or n == "4" or\
#            n == "5" or n == "6" or n == "7" or n == "8" or n == "9":
#             nu += 1
#     file2.write("nums " + str(nu))

######################################################################################################
# deleting the last line from a text file, and writing the result to another file

# file1 = open("text1.txt", "r")
# file2 = open("text2.txt", "w")
# with file1, file2:
#     data = file1.readlines()
#     del data[-1]
#     file2.writelines(data)

#####################################################################################################
# getting the length of the longest row in text file

# file1 = open("text1.txt")
# with file1:
#     lines = file1.readlines()
#     print("Longest line:", len(max(lines, key=len)))

#####################################################################################################
# getting specified word's number

# file1 = open("text1.txt", "r")
# with file1:
#     data = file1.read().lower().split()
#     word = input('Word to count: ')
#     print("Number of", '"' + word + '":', data.count(word))

#####################################################################################
# Editing a text file: adding line "********" after the last line, that contains coma.
# If there is no line with coma, adding "********" as a last line. Result - to another file.

# file1 = open("text1.txt")
# with file1:
#     list1 = []
#     data = file1.readlines()[::-1]
#     for c in data:
#         list1.append(c)
#         if "," in c:
#             list1.insert(-1, "********\n")
#             break
#     else:
#         list1.insert(0, "\n********")
#     for c in data:
#         if c not in list1:
#             list1.append(c)
# file2 = open("text2.txt", "w+")
# with file2:
#     file2.writelines(list1[::-1])

#########################################################################################
# Changing all * on & and vice versa in a text file

# file = open("text1.txt")
# with file:
#     fileR = file.read()
#     fileR = fileR.replace("*", "%%").replace("&", "*").replace("%%", "&")
# file = open("text1.txt", "w")
# with file:
#     file.write(fileR)

#########################################################################################
# Writing every element of list of strings on a new line in a text file.

# array = ["Text line1", "Text line2",
#          "Text line3", "Text line4",
#          "Text line5", "Text line6"]
# text = [c + "\n" for c in array]
# file1 = open("text2.txt", "w")
# with file1:
#     file1.writelines(text)
