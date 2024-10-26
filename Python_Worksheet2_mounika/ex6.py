#6 program to extract elements of a list, if it occurs more than k times.
from random import randint

rand_list=[randint(5,10) for i in range(20)]
print('random list:',rand_list)
k=int(input('enter occurrence number :'))
extract_elements={e: rand_list.count(e) for e in rand_list if rand_list.count(e) >k}
keys=list(extract_elements.keys())
print(f'In the given list elements:{keys} occurred more than {k} times')