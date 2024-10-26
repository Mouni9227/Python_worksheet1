#program to find the even numbers in a list, L.
from random import randint

#random generation of list
rand_len=randint(5,10)
print('length of the list=',rand_len)
rand_list=[randint(10,25) for _ in range(rand_len)]
print(rand_list)

even=[i for i in rand_list if i%2==0 ]
print(f'Even number in the list are ={even}')
