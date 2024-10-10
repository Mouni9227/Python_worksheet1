#function to convert decimal to binary
from math import remainder

def get_binary(d):
    #getting binary from built-in function
    binary=bin(d)[2:]
    return binary

def main():
    d=int(input("Enter a Decimal number: "))
    print(f'The binary representation of {d} is' ,get_binary(d))

    #getting binary manually
    decimal=int(input("enter a decimal: "))
    binary=""
    while decimal>0:
        remainder=decimal%2
        binary=binary+str(remainder)
        decimal=decimal//2
    print("binary representation:",binary[::-1])


if __name__ == "__main__":
    main()