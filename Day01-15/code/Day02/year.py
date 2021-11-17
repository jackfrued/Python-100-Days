a = int(input('year = '))
b = (a%4 == 0 and a%100 !=0 or a%400 == 0)
print(b)