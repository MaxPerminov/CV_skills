import datetime
import random


# creating a list of random birthdays:
birthdays = []
for i in range(3):  # number of birthdays
    birthdays.append(datetime.date(1923, 1, 1) + datetime.timedelta(random.randint(0, 364*100)))

print("1)list of birthdays in format of <datetime>'s method date():\n", birthdays,
      "\n________________________________________")
print("2)getting a birthday by index:\n", birthdays[0],
      "\n________________________________________")
print("3)getting a birthday, month, year:\n", birthdays[0].day, birthdays[0].month, birthdays[0].year,
      "\n________________________________________")
print("4)Printing all the birthdays: ")
for i in birthdays:
    print(i)

print("\n\n")

# +- to date:
print(datetime.date(2023, 5, 1) - datetime.timedelta(days=2))   # 2023-04-29
print(datetime.date(2023, 5, 1) + datetime.timedelta(days=10000))   # 2050-09-16
print(datetime.date(2023, 2, 21) - datetime.date(1984, 11, 6))  # 13986 days, 0:00:00
print(datetime.date(2023, 2, 21) - datetime.date(1, 1, 1))  # 738571 days, 0:00:00

# weekday
print(datetime.date(1984, 11, 6).weekday())  # 1(Tuesday), because Monday is 0 and Sunday is 6.

# getting int - year, month, day
print(datetime.date(1995, 6, 19).year)
print(datetime.date(1995, 6, 19).month)
print(datetime.date(1995, 6, 19).day)
