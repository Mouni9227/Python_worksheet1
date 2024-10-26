#function to find the sum and average of numbers in a list
from random import randint, random

#random generation of list
rand_len=randint(5,10)
print('length of the list=',rand_len)
rand_list=[randint(10,25) for _ in range(rand_len)]
print(rand_list)

#sum using in built function
summation=sum(rand_list)
avg=round(summation/rand_len,2)
print(f'summation= {summation}')
print(f'average  = {summation}/{rand_len} = {avg}')

# #using normal loop format
# summation=0
# for i in rand_list:
#     summation+=i
# print('\nsum',summation)
# print('avg',summation/rand_len)
#
# #using list comprehension
# total=0
# res=[total :=total +i for i in rand_list]
# print('\nsum',total)
# print('avg',total/rand_len)



