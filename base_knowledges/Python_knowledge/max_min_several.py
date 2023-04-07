import heapq

grades = [5, 75, 6, 30, 95, 1005.2, 745, 1.9, 112, 809.5]
print(heapq.nlargest(5, grades))
print(heapq.nsmallest(2, grades))

