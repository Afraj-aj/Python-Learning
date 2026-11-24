rows = 5
for i in range(1, rows + 1):
    spaces = " " * ( rows - i )
    stars = "* " * i
    print(spaces + stars)

for j in range(1, rows + 1):
    for k in range(rows - j):
        print(" ", end="")
    for l in range(2 * j - 1):
        print("*", end="")
    print()


for a in range(1, rows + 1):
    for b in range(rows - a):
        print("", end="")
    for c in range(a):
        print("*", end=" ")
    print()

for a in range(1, rows + 1):
    for b in range(rows - a):
        print(" ", end="")
    for c in range(a):
        print("*", end=" ")
    print()

for a in range(1, rows + 1):
    for b in range(rows - a):
        print(" ", end=" ")
    for c in range(a):
        print("*", end=" ")
    print()