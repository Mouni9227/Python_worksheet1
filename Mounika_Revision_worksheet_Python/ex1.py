#volume of cylinder
from math import pi

def main():
    r=int(input("Enter the radius of the cylinder: "))
    h=int(input("Enter the height of the cylinder: "))
    v=(pi*r**2)*h
    print(f'The volume of the cylinder is: ',round(v,2))

if __name__ == "__main__":
    main()


