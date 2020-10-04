# DOUBLING NUMBERS
from random import randint

original = [randint(1, 100) for i in range(10)]
doubled = [i*2 for i in original]
doubled_mapped = list(map(lambda i: i*2, original))

print('original list by list comprehension: ', original)
print('doubled list by list comprehension:  ', doubled)
print('double list by mapping:              ', doubled_mapped)
print('')

# LENGTH, VOWELS IN NAMES

def vowels_in_name(name):
    name = name.lower()
    vowels = 'aeiou'
    count = 0
    for letter in name:
        if letter in vowels:
            count += 1
    return count

names = ['Joseph', 'Jessica', 'Xiao', 'Sakura', 'Krish', 'Julia']
length = list(map(len, names))
vowels = list(map(vowels_in_name, names))

print('Names:                     ', names)
print('Length of names:           ', length)
print('Number of vowels in names: ', vowels)