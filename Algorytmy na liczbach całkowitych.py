from math import isqrt


def itostr(num: int, base: int):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    out = ''
    while num != 0:
        ind = num % base
        out += digits[ind]
        num //= base
    return out[::-1]


def isPrime(num):
    for i in range(2, isqrt(num)):
        if num % i == 0:
            return False
    return True

def isIdeal(num):
    if num == 1: return False
    denominators = [1]
    for i in range(2, isqrt(num)+1):
        if num % i == 0:
            denominators.extend([i, num//i])

    print(denominators)
    return sum(denominators) == num

def primeFactors(num):
    i = 2
    factors = []
    while i <= num:
        if num % i == 0:
            factors += [i]
            num //= i
        else:
            i += 1
    return factors

# print(primeFactors(24))
# print(primeFactors(100))


def fibrec(num):
    if num ==0 or num == 1:
        return 1
    return fibrec(num-1) + fibrec(num-2)
def fib(num):
    last = 1
    curr = 1
    next = 0
    for i in range(num -1):
        next = curr+last
        last = curr
        curr = next
    return curr

# print(fib(2))
# print(fib(3))
# print(fib(5))

def dealChange(ammount, monetary_values):
    monetary_values.sort()
    change = []
    for i in monetary_values[::-1]:
        while ammount >= i:
            ammount -= i
            change += [i]
    return change

print(dealChange(6, [4, 3, 1]))

def gcdrec(a, b):
    if a == 0: return b
    if b == 0: return a
    if a == b: return a
    gcdrec(b, a%b)

def gcd(a,b):
    while b!=0:
        a,b =b, a%b
    return a


