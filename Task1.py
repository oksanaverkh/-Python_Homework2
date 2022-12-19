# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import os
os.system('cls')

num = float(input('Enter a number: '))
sum_num_digits = 0

if num<0:
    num = num*-1
else: 
    num = num

if num % 1 == 0:
    while num > 0:
        sum_num_digits += num % 10
        num = num//10
    print("Sum of number's digits = ", sum_num_digits)

else:
    num = str(num)
    n = []
    n = num.split('.')
    new_n = []
    for i in range(len(n)):
        new_n.append(int(n[i]))
        while new_n[i] > 0:
            sum_num_digits += new_n[i] % 10
            new_n[i] = new_n[i]//10
    print("Sum of number's digits = ", sum_num_digits)

