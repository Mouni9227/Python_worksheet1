#replace character
def main():
    string=input("Enter two words separated by comma: ")

    if ',' not in string:#error check if user not provides comma
        print("Error : Please enter comma separated words ")
        return
    if any(char.isdigit() for char in string): #error check if user provides numerical strings
        print("Invalid! Please enter only non numeric strings.")
        return

    char=input("Enter a character you want to replace: ")
    new_char=input("Enter a new character: ")
    new_char=new_char.center(5) # center justification done to get good visualization of modified string
    print(f'The modified string is',string.replace(char, new_char))

if __name__ == "__main__":
    main()