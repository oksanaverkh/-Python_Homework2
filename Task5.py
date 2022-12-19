# Реализуйте алгоритм перемешивания списка.

import os
import random
os.system('cls')

n = int(input('Enter number N: '))
limit = int(input('Enter limit: '))

my_list = []
for i in range(n):
    my_list.append(random.randint(-limit, limit))
print('List of N-elements:', my_list)

#Variant1
random.shuffle(my_list)
print('Mixed list of N-elements (variant1):', my_list)

#Variant2
mixed_list = []
for ii in range(n):
    if ii < n//2:
        mixed_list.append(my_list[n-ii-1])
    else:
        mixed_list.append(my_list[ii-n//2])
print('Mixed list of N-elements (variant2):', mixed_list)


