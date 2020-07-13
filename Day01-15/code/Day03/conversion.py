"""
英制单位英寸和公制单位厘米互换

"""
a = float(input('number = '))
b = input('unit is ')

if b == 'in' or b == 'inch':
    c = a * 2.54
    print('%.2f in is %.2f cm' % (a, c))
elif b == 'cm':
     c = a / 2.54
     print('%.2f cm is %.2f in' % (a, c))
else:
    print ('unit not identified')