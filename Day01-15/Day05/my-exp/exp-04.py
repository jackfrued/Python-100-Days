"""
Author: Tang

Date: 2019-05-16

"""
def feib():
    a = 1
    b = 0
    for i in range(1,50):
        print("{}".format(a))
        b = a + b
        a, b = b, a



if __name__=="__main__":
    feib()