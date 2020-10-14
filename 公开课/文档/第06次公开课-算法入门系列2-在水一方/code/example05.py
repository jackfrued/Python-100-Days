size = 25

for i in range(size):
    for j in range(size):
        if i % 2 == 1 or j % 2 == 1:
            print('■', end='')
        else:
            print('□', end='')
    print()
 
