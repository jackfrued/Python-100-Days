"""
Author: Tang

Date: 2019-05-16

"""
import math

for num in range(1,1000):

    sum = 0
    for factor in range(1,int(math.sqrt(num))+1):
        if num % factor == 0:
            sum += factor
            
            if factor > 1 and num / factor != factor:
                sum += num / factor
        

    if num == sum:
        print("{} 是完美数".format(num))

