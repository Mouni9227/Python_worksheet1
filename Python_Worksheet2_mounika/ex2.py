#function to find the minimum and maximum number in a list, L.

from random import randint

#random generation of list
rand_len=randint(5,10)
print('length of the list=',rand_len)
rand_list=[randint(10,25) for _ in range(rand_len)]
print(rand_list)

maximum=0
for i in range (0,len(rand_list)-1):
    if rand_list[i] > maximum:
        maximum=rand_list[i]
print(f'maximum number in the list ={maximum}')

minimum=10000
for i in range(0,len(rand_list)-1):
    if rand_list[i] < minimum:
        minimum=rand_list[i]
print(f'minimum number in the list ={minimum}')

