#3, count no of 1s in binary representation of decimal N
def count_1s(n):
     count = bin(n).count('1')
     return count

def main():
     n=int(input('enter a decimal number: '))
     print(f' the total number of 1s in binary representation of {n}  is', count_1s(n))

if __name__ =="__main__":
    main()