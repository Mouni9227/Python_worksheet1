def check_anagrams(s1,s2):
    if list(s1).sort == list(s2).sort:
        return True
    else:
        return False

def main():
    s1= input("Enter a string: ")
    s2= input("Enter another string: ")
    if len(s1) != len(s2):
        print(f'Given strings are different lengths.so,{s1} and {s2} are not anagrams')
    else:
        print(f'Both {s1} & {s2} are Anagrams:', check_anagrams(s1,s2))

if __name__ == "__main__":
    main()