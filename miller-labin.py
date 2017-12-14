import random
import math

_mrpt_num_trials = 100  # number of bases to test


def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert (2 ** s * d == n - 1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True  # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True  # no base tested showed n as composite


def find_next_prime(n):
    if n % 2 == 0:
        n += 1
    i = 0
    while False == is_probable_prime(n):
        n += 2
        i += 1
        if i > 50000:
            break;
            return 0
    print "loop used=%d, %d" % (i, i * 2 + 2)
    return n

def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1

def prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


#inn = random.uniform(10**17, 9 * 10**17)
inn = 10**180
if False == is_probable_prime(int(inn)):
    print "not prime"
else:
    print "may be prime"
temp = find_next_prime(int(inn))
print temp
print inn
print prime(3758572721726699537)