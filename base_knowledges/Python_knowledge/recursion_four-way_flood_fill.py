#  There is a green area. It has a blue frame.
color_desk = {
              (0, 0): 'blue', (0, 1): 'blue', (0, 2): 'blue', (0, 3): 'blue', (0, 4): 'blue',
              (1, 0): 'blue', (1, 1): 'green', (1, 2): 'green', (1, 3): 'green', (1, 4): 'blue',
              (2, 0): 'blue', (2, 1): 'green', (2, 2): 'green', (2, 3): 'green', (2, 4): 'blue',
              (3, 0): 'blue', (3, 1): 'green', (3, 2): 'green', (3, 3): 'green', (3, 4): 'blue',
              (4, 0): 'blue', (4, 1): 'blue', (4, 2): 'blue', (4, 3): 'blue', (4, 4): 'blue'
}


# printing color desk
def paint(arr):
    print(arr[0, 0], arr[0, 1], arr[0, 2], arr[0, 3], arr[0, 4])
    print(arr[1, 0], arr[1, 1], arr[1, 2], arr[1, 3], arr[1, 4])
    print(arr[2, 0], arr[2, 1], arr[2, 2], arr[2, 3], arr[2, 4])
    print(arr[3, 0], arr[3, 1], arr[3, 2], arr[3, 3], arr[3, 4])
    print(arr[4, 0], arr[4, 1], arr[4, 2], arr[4, 3], arr[4, 4])


def change_color(color, arr, x, y, previous_color):
    arr[(x, y)] = color
    if x < 4 and arr[(x + 1, y)] == previous_color:
        change_color(color, arr, x + 1, y, previous_color)
    if y < 4 and arr[(x, y + 1)] == previous_color:
        change_color(color, arr, x, y + 1, previous_color)
    if x > 0 and arr[(x - 1, y)] == previous_color:
        change_color(color, arr, x - 1, y, previous_color)
    if y > 0 and arr[x, y - 1] == previous_color:
        change_color(color, arr, x, y - 1, previous_color)


paint(color_desk)
# change_color("red", color_desk, 1, 1, "green")  # changes green to red
# change_color("red", color_desk, 0, 0, "blue")  # changes blue to red
print()
paint(color_desk)
