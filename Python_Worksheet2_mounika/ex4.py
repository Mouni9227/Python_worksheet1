#program to print the duplicate elements in a list, L.
from random import randint, random

#random generation of list
rand_len=randint(5,10)
print('length of the list=',rand_len)
rand_list=[randint(10,25) for _ in range(rand_len)]
print(rand_list)

d=[ i for i in rand_list if rand_list.count(i)>=2]
d=set(d)
print('The duplicate elements in the list',d)