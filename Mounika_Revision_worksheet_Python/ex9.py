#check triangle formed or not using triangle inequality law
def main():
    a=int(input("Enter the side 1 of triangle: "))
    b=int(input("Enter the side 2 of triangle: "))
    c=int(input("Enter the side 3 of triangle: "))

    if a<=0 or b<=0 or c<0: #error check
        print("Invalid! Please provide non_zero , non-negative numbers")
        return

    if a+b>c and b+c>a and c+a>b:#triangle inequality law
        if a==b==c:
            print("The given sides will form Equilateral Triangle")
        elif a==b!=c or b==c!=a or c==a!=b:
            print("the given sides will form Isosceles Triangle")
        elif a!=b!=c or b!=c!=a or c!=a!=b:
            print("the given sides will form Scalene Triangle")
    else:
        print("Sorry, can't form a triangle with given values. HINT:'Triangle inequality law'")

if __name__ == "__main__":
    main()
