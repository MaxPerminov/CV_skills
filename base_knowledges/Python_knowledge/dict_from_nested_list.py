def students_dict_fn(*x):
    y = {}
    y.update(x)
    return y


students = [
    [
        "John", 2323
    ],
    [
        "Mike", 3232
    ],
    [
        "Leslie", 6000
    ]
]
students_dict = {}
for i in students:
    students_dict.update(students_dict_fn(i))

print(students_dict)
