#program to extract words from a string list, L whose first character is k.

string_list=input('Enter strings:')
string_list=list(string_list.split())
first_char=input('Enter a first character of word you want to extract:')
word=[i for i in string_list if i[0]==first_char]
print(f'First character "{first_char}" containing words are :{word}')