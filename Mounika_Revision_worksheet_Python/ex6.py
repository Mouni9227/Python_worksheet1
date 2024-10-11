#math operations
from termios import INPCK
def math_operations(n1,n2):
    addition = n1 + n2
    product = n1 * n2
    difference = n1 - n2
    quotient = n1 / n2
    remainder = n1 % n2
    print(f'The sum of {n1} and {n2}        = ',addition)
    print(f'The product of {n1} and {n2}    = ',product)
    print(f'The difference of {n1} and {n2} = ',difference)
    print(f'The quotient of {n1} and {n2}   = ',quotient)
    print(f'The remainder of  {n1} and {n2} = ',remainder)

def main():
    n1=int(input("Enter a number 1: "))
    n2=int(input("Enter a number 2: "))
    print(math_operations(n1,n2))

if __name__ == "__main__":
    main()