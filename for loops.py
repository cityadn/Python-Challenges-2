n = 3
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')

print("\n")

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')

print('\n')

for i in range(1, 11):
    print(i)
