# Number Diamond Pattern Program
# Created by: Dhanesh Kumar Jain

n = int(input('Enter any number: '))

# Upper part
for i in range(1, n+1):
    a = 1
    print(' ' * (n - i), end='')

    for j in range(2*i - 1):
        print(a, end='')
        a = a + 1 if a < i else a - 1
    print()

# Lower part
for i in range(n-1, 0, -1):
    a = 1
    print(' ' * (n - i), end='')

    for j in range(2*i - 1):
        print(a, end='')
        a = a + 1 if a < i else a - 1
    print()
