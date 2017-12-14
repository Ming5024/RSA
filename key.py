#!/usr/bin/python3.5
# -*- coding:  UTF-8-*-
import random
from random import randrange
from math import sqrt
import tkinter

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a

def exEuclidean(en, eb):
    if (eb > en):
        en, eb = eb, en
    r1 = en
    r2 = eb
    t1 = 0
    t2 = 1
    while(r2 > 0):
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t
    if(r1 == 1):
        return t1 % en

def fast_Exponentiation(a, b, c):
    a_1 = a % c
    ans = 1
    while(b):
        if b % 2 == 1:
            ans = (ans * a_1) % c
        a_1 = (a_1 * a_1) % c
        b = b>>1
    return ans

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def isprime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

def is_prime(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def next_prime(num):
    if (not num & 1) and (num != 2):
        num += 1
    if is_prime(num):
        num += 1
    while True:
        if is_prime(num):
            break
        num += 2
    return num

def makeKey():
    inn = random.uniform(2 ** 511, 2 ** 512 - 1)
    p = next_prime(int(inn))
    inn = random.uniform(2 ** 511, 2 ** 512 - 1)
    q = next_prime(int(inn))
    print('p =', p)
    print('q =', q)
    n = p * q
    t_n = (p - 1) * (q - 1)
    e = 65537
    for i in range(65537, 100000):
        if (gcd(t_n, i) == 1):
            e = i
            break
    d = exEuclidean(t_n, e)
    text_n.delete(1.0, tkinter.END)
    text_n.insert(tkinter.END, str(n))
    text_e.delete(1.0, tkinter.END)
    text_e.insert(tkinter.END, str(e))
    text_d.delete(1.0, tkinter.END)
    text_d.insert(tkinter.END, str(d))

if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('RSA密钥生成器')
    window.geometry('600x500')

    l1 = tkinter.Label(window, text='n:', font=("Monospace", 11), width=15, height=3)
    l1.pack()

    text_n = tkinter.Text(window, font=("Helvetica", 12), width=55, height=7)
    text_n.pack()

    l2 = tkinter.Label(window, text='e:', font=("Monospace", 11), width=15, height=3)
    l2.pack()

    text_e = tkinter.Text(window, font=("Helvetica", 12), width=55, height=2)
    text_e.pack()

    l3 = tkinter.Label(window, text='d:', font=("Monospace", 11), width=20, height=3)
    l3.pack()

    text_d = tkinter.Text(window, font=("Helvetica", 12), width=55, height=7)
    text_d.pack()

    button = tkinter.Button(window, text="Create Key", font=("Monospace", 12), width=15, height=2, command=makeKey)
    button.place(x=200, y=440, anchor=tkinter.NW)
    # button.pack()

    window.mainloop()