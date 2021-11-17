a = float(input('number = '))
b = input('unit is ')

if b == 'in' or b == 'inch':
    c = a * 2.54
    print(f'{a} {b} is {c} cm')
elif b == 'cm':
     c = a / 2.54
     print('%.2f cm is %.2f in' % (a, c))
else:
    print ('unit not identified')