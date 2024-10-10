#5,compute power raise base to the nth power
def compute_power(base,power):
    result=base**power
    return result

def main():
    base=int(input('Enter base number: '))
    power=int(input('Enter power: '))
    print(f' The value of {base} power {power} is' , compute_power(base,power))

if __name__ =="__main__":
    main()
