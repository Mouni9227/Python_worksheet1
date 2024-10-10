#function to find the first occurrence of a character, c, in a string S.
def main():
   s=input("Enter a string: ")
   c=input("Enter a character: ")
   occurrence=s.find(c)
   print(f'The first occurrence index of character ({c}) in the {s} is ', occurrence)

if __name__ =="__main__":
   main()