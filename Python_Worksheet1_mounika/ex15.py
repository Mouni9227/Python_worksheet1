def main():
    string = input("Enter a sentence: ")
    word=input("Enter a word you want to count: ")
    print(f'The total count of number of occurrences of a {word} are :',string.count(word))

if __name__ == "__main__":
    main()
