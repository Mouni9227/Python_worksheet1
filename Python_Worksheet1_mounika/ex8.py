def get_half_string(s):
    half=s[:len(s)//2]
    return half

def main():
   s=input("Enter a string: ")
   print(f'The first half of the string', get_half_string(s))

if __name__ =="__main__":
   main()