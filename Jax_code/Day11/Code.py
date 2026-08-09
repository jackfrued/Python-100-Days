from math import sqrt

def is_prime(n):
    assert n > 0, f'Prime number ain\'t negative'
    for factor in range(2, int(sqrt(n) + 1)):
        if n % factor == 0:
            return False
    return True if n != 1 else False
    
def main():
    number = int(input("Input a number:\n"))
    print(is_prime(number))


if __name__ == '__main__':
    main()