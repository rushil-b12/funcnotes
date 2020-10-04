from functools import reduce
from random import randint
from filtering import is_prime

# MULTIPLYING NUMBERS

def multiply(to_multiply):
    total = 1
    for number in to_multiply:
        total = total*number
    return total

numbers = [randint(1, 20) for i in range(5)]
print('numbers:    ', numbers)
print('multiplying:', multiply(numbers))

# SUMMING PRIME NUMBERS

def adding(to_add):
    total = 0
    for number in to_add:
        total += number
    return total

prime = [i for i in range(2, 101) if is_prime(i)]
print('numbers:        ', prime)
print('adding (long):  ', adding(prime))
print('adding (short): ', sum(prime))

# SUMMING DIGITS

def sum_digits(number):
    while number > 9:
        number = sum(int(i) for i in str(number))
    return number
    

# numbers_to_add = [19, 9, 11, 15, 9]
single_digits = [sum_digits(x) for x in prime]
total = sum(single_digits)
final = sum_digits(total)

print('numbers:       ', prime)
print('single digits: ', single_digits)
print('total:         ', total)
print('final total:   ', final)