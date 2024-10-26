#program to remove all occurrences of an element from a list, L.
from random import randint

rand_list=[randint(5,10) for i in range(10)]
print('Original list:',rand_list)
n=int(input('Enter a number to be removed in the list:'))
if n not in rand_list:
    print('Invalid, please try again with another number provided in the list!')
else:
    new_list_element=[i for i in rand_list if n!=i ]
    print(f'List after removing all occurrences of {n} is {new_list_element}')