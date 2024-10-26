#Remove all duplicate words from given sentence using a dictionary

def remove_dup_words(s):
    dict = {}
    unique_words = []

    for word in s:
        word = word.lower()
        if word not in dict:
            dict[word] = 1
            unique_words.append(word)

    return ' '.join(unique_words)

def main():
    s = input('Enter a sentence: ')
    s = s.split()
    print(f'Sentence after removing duplicate words: {remove_dup_words(s)}')

if __name__ == "__main__":
    main()

