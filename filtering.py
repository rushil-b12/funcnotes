# PRIME NUMBERS
def is_prime(x):
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

prime = []

# for i in range(2, 101):
#         if is_prime(i):
#             prime.append(i)

prime = [i for i in range(2, 101) if is_prime(i)]
prime_filtered = list(filter(is_prime, range(2, 101)))
if __name__ == '__main__':
    print('using list comprehension: ', prime)
    print('using filter:             ', prime_filtered)

# NAMES WITH A
def is_a(name):
    if name[0].lower() == 'a':
        return True
    return False

names = ['Albert', 'betty', 'Anna', 'andrew', 'Evie', 'harrison', 'Daniel', 'avani']
starts_with_a = [name for name in names if is_a(name)]
starts_with_a_but_filter = list(filter(lambda name: name[0].lower() == 'a', names))
if __name__ == '__main__':
    print('using list comprehension: ', starts_with_a)
    print('using filter:             ', starts_with_a_but_filter)

