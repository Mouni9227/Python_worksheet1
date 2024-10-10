#function to get sum of squares of first N numbers
def sum_of_squares(n):
    sum=0
    for i in range(0,n+1):
        square=i**2
        sum=sum+square
    return sum

def main():
    n=int(input("Enter a number: "))
    print(f'The sum of squares of first {n} numbers is' , sum_of_squares(N))

if __name__ == "__main__":
    main()