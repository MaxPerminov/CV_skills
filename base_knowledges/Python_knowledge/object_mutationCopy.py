# It is possible to create several
# variables with the same reference to the object. And changes in the
# object's properties from a side of any the variable will affect on the
# object, hence, on all the variables.


john = {
    "name": "John",
    "age": 23,
    "relative": {
        "name": "Mike",
        "age": 13
    }
}
print(john)

mike = john["relative"]
mike["age"] = 32  # age changes in both vars - john and mike(vars refer to one object)
print(mike)

print(john)

print()

john = {
    "name": "John",
    "age": 23,
    "relative": {
        "name": "Mike",
        "age": 13,
    }
}
print(john)

mike = john["relative"].copy()
mike["age"] = 32  # age changes only in mike
print(mike)

print(john)
