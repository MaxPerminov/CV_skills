studGroup1 = {"Hanna", "Joe", "Kate"}
studGroup2 = {"Bob", "Joe", "Jane", "Kate"}

# intersection - returns a set that contains the similarity between two or more sets.
print(studGroup1 & studGroup2)
# or
print(studGroup1.intersection(studGroup2))


# union - returns a set that contains all items from the original set, and all items from the specified set(s).
print(studGroup1 | studGroup2)
# or
print(studGroup1.union(studGroup2))


# difference - returns a set that contains the difference between two sets.
print(studGroup1 - studGroup2)
# or
print(studGroup1.difference(studGroup2))

##################################################################
userApp1 = ["user134", "admin56", "superBob",
            "student", "spider34"]
userApp2 = ["fifa56", "user134", "stuGood",
            "admin56", "spider34"]

# applying it to lists
print(set(userApp1) & set(userApp2))
print(set(userApp1) - set(userApp2))
print(set(userApp2) - set(userApp1))
print(set(userApp1) | set(userApp2))
