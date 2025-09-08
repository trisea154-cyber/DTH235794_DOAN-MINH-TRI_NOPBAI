def print_hollow_square(n):
    if n <= 0:
        return
    print('*' * n)
    for _ in range(n-2):
        print('*' + ' ' * (n-2) + '*'
    if n > 1:
        print('*' * n)
print_hollow_square(4)