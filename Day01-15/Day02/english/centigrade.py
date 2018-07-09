"""

Convert Fahrenheit to Celcius
F = 1.8C + 32

Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""

f = float(input('Please enter Fahrenheit temperature: '))
c = (f - 32) / 1.8
print('%.1fFahrenheit = %.1fCulcius' % (f, c))
