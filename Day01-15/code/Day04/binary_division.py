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
print(li)
# # convert to int list
# bi = []
# for i in range(len(li)):
#     a = int(li[i])
#     bi.append(a)
# print(bi)
# di = []
# c = 0
# for i in range(len(di)):
#     for digit in di[i]:
#         c = c*2 + int(digit)
#         di.append(c)

# print(di)
# c = 0
# di = []
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         c = c + pow(2, j)
#         di.append(c)
#     i += 1
# print(di)
di = []
for i in range(len(li)):
    for j in li[i]:
        base = 1
        sum = 0
        for digit in li[i]:
            sum += base *2*int(digit)
            base*2
            di.append(j)
    i += 1
print(di)


# print the numbers that are divisible by 5
i = 0
while i <= len(li):
    if di[i] % 5 == 0:
        print(li[i])
        break
    i += 1 
else:
    print('non is divisible by 5')