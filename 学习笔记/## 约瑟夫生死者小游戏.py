lst1 = [1,2,3,4,5]

for i in lst1:
    if i % 2 == 0:
        lst1.pop(i)

print(lst1)