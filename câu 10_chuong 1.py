width = 11

patterns = [1, 3, 7, 3, 5, 11 ]
for stars in patterns:
    spaces = (width - stars) // 2
    print(" " * spaces + "*" * stars)


for _ in range(2):
    print(" " * 4 + "* *")