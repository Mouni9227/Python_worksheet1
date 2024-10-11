#The median calculation
from statistics import median

def main():
    val1=int(input("Enter first number: "))
    val2=int(input("Enter second number: "))
    val3=int(input("Enter third number: "))
    l=[val1,val2,val3]
    print(f'The median of {val1},{val2},{val3} is : ',median(l))#getting median from built-in function
# we can get the median by sorting the list and getting the middle number without importing median from stats
#     l.sort()
#     m=l[len(l)//2]
#     print(f'The median is',m)


if __name__ == "__main__":
    main()