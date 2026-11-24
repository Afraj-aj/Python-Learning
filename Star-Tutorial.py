rows = 5

print("Left-aligned triangle:")
for i in range(1, rows + 1):
    print("* " * i)

print("\nCentered pyramid:")
for j in range(1, rows + 1):
    for k in range(rows - j):
        print(" ", end="")
    for l in range(2 * j - 1):
        print("*", end="")
    print()

print("\nRight-aligned triangle:")
for a in range(1, rows + 1):
    for _ in range(rows - a):
        print(" ", end="")
    for _ in range(a):
        print("*", end="")
    print()

print("\nCentered triangle with spaced stars:")
for i in range(1, rows + 1):
    print("  " * (rows - i) + "* " * i)