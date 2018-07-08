"""

String common operations

Version: 0.1
Author: 骆昊
Date: 2018-02-27

"""

str1 = 'hello, world!'
print('Length of string str1 is:', len(str1))
print('Title cased string: ', str1.title())
print('String is Converted to uppercase: ', str1.upper())
# str1 = str1.upper()
print('is the string uppercase : ', str1.isupper())
print('Does the string start with hello: ', str1.startswith('hello'))
print('Does the string end with hello: ', str1.endswith('hello'))
print('Does the string start with "!": ', str1.startswith('!'))
print('Does the string end with "!": ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
