#hypotenuse of right angled triangle
from math import sqrt

def main():
    a=int(input("Enter the side1 of right angled triangle: "))
    b=int(input("Enter the side2 of the right angled triangle: "))
    # c=sqrt(a**2+b**2) #by importing sqrt
    c=int((a**2+b**2)**0.5)
    print(f'The hypotenuse of right angled triangle is: ',c)

if __name__ == "__main__":
    main()
