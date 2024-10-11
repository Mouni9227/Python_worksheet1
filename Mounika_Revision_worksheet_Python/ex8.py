#indefinite articles
def main():
    word=input("Enter a word(noun): ")
    word=word.lower()  #lowered the case to avoid case-sensitive errors
    word=word.split()  #removing leading white spaces if incase my user provides a string starts with space

    if any(char.isdigit() for char in word): #erroe check if user provides numbers
        print("Invalid! Please enter only non numeric strings.")
        return

    vowel='aeiou' #assigned vowels to a variable
    if word[0] in vowel: #sliced starting index position to check the vowels
        print("The indefinite article should be 'An'")
    else:
        print("The indefinite article should be 'a'")

if __name__ == "__main__":
    main()
