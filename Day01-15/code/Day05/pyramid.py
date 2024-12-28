#lets start with simple right angle triangle
n = int(input("enter number of rows: "))
# n is a veriable for taking number of rows 
for x in range (0,n):

    for y in range (0,x+1):

        print("* ",end = "")

    print("\r")
