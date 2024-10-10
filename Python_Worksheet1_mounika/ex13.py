def main():
    string=input("Enter a string: ")
    char=input("Enter a character you want to replace: ")
    new_char=input("Enter a new character: ")
    print(f'The modified string is',string.replace(char, new_char))

if __name__ == "__main__":
    main()