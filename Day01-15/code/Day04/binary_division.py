"""
Write a Python program which accepts a sequence of comma separated n digit binary numbers as 
its input and print the numbers that are divisible by 5 in a comma separated sequence

sample input: 0100,0011,1010,1001,1100,1001
sample output: 1010

"""

# input comma separated elements as string 
str = str (input ("Enter comma separated integers: "))

# conver to the list
list = str.split (",")

# convert each element as integers
li = []
for i in list:
    li.append(i)
#print(li)
di = []
for i in range(len(li)):
    a = int(li[i], 2)
    di.append(a)
    i += 1
#print(di)

# print the numbers that are divisible by 5
i = 0
while i <= len(li):
    if di[i] % 5 == 0:
        print(li[i])
        break
    i += 1 
else:
    print('non is divisible by 5')