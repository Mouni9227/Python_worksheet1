#check prime or composite
def main():
    n = int(input("Enter a number: "))
    if n == 1:
        print("Given number is neither a prime nor a composite")
        return
    elif n == 2:
        print("2 is a prime number.")
        return
    elif n <= 0:
        print("Please enter a non-zero , non_negative number")
        return
    else:
        for i in range(2,n):
            if n%i ==0:
                print("It is a composite number.")
                return
        print("It is a prime number")

if __name__ == "__main__":
    main()


# def check_prime(n):
#     for i in range(2,n):
#         if n%i ==0:
#             return False
#     return True
#
# def main():
#     n = int(input("Enter a number: "))
#     if n==1:
#         print("Given number is neither a prime nor a composite")
#     elif n<=0:
#         print("Please enter a non-zero , non_negative number")
#     else:
#         print(f'{n} is a prime number',check_prime(n))
#
# if __name__ == "__main__":
#     main()