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

def encrypt(plain, e, n):
    cipher = fast_Exponentiation(plain, e, n)
    return cipher

def decrypt(cipher, d, n):
    plain = fast_Exponentiation(cipher, d, n)
    return plain

def RSA():
    '''''
    global p,q,e,d,n
    inn = random.uniform(2 ** 511, 2 ** 512 - 1)
    p = next_prime(int(inn))
    inn = random.uniform(2 ** 511, 2 ** 512 - 1)
    q = next_prime(int(inn))
    n = p * q
    print (p)
    print (q)
    t_n = (p - 1) * (q - 1)
    e = 65537
    for i in range(65537, 100000):
        if(gcd(t_n, i) == 1):
            e = i
            break
    d = exEuclidean(t_n, e)
    print('e =', e)
    print('d =', d)
    '''''
    e = text_e.get("1.0", "end-1c")
    e = int(e)
    n = text_n.get("1.0", "end-1c")
    n = int(n)
    plaintext = plaintextInput.get("1.0", "end-1c")
    plainnum = ''
    ciphertextOutput.delete(1.0, tkinter.END)

    i = 0
    while i < len(plaintext):
        temp_num = 0
        num = ord(plaintext[i])
        temp = str(num)
        #print (temp)
        if (len(temp) == 5):
            result_temp = '9' + temp
        else:
            while (len(temp) < 3):
                temp += ' '
                temp_num += 1
            result_temp = ''
            if (temp_num > 0):
                result_temp = '8'
            for r in range(0, temp_num - 1):
                result_temp += '0'
            result_temp += str(num)
        #print (result_temp)
        plainnum += result_temp
        i += 1

    #print(plainnum)
    while(len(plainnum) % 100 != 0):
        plainnum += '0'
    #print ('plainnum =', plainnum)
    i = 1
    temp_plain = ''
    while i < len(plainnum) + 1:
        temp_plain += plainnum[i-1]
        if (i % 100 == 0 and i != 0):
            int_plainnum = int(temp_plain)
            #print('plainnum =', temp_plain)
            ciphernum = encrypt(int_plainnum, e, n)
            #print('ciphernum =', ciphernum)
            ciphertextOutput.insert(tkinter.END, str(ciphernum))
            ciphertextOutput.insert(tkinter.END, ',')
            temp_plain = ''
        i += 1


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('RSA加密器')
    window.geometry('600x600')

    l1 = tkinter.Label(window, text='e:', font=("Monospace", 11), width=15, height=2)
    l1.pack()

    text_e = tkinter.Text(window, font=("Helvetica", 12), width=55, height=2)
    text_e.pack()

    l2 = tkinter.Label(window, text='n:', font=("Monospace", 11), width=15, height=2)
    l2.pack()

    text_n = tkinter.Text(window, font=("Helvetica", 12), width=55, height=6)
    text_n.pack()

    l3 = tkinter.Label(window, text='Plaintext:', font=("Monospace", 11), width=20, height=2)
    l3.pack()

    plaintextInput = tkinter.Text(window, font=("Helvetica", 12), width=55, height=7)
    plaintextInput.pack()

    l4 = tkinter.Label(window, text='Ciphertext:', font=("Monospace", 11), width=20, height=2)
    l4.pack()

    ciphertextOutput = tkinter.Text(window, font=("Helvetica", 12), width=55, height=7)
    ciphertextOutput.pack()

    button = tkinter.Button(window, text="Encrypt", font=("Monospace", 12), width=15, height=2, command=RSA)
    button.place(x=200, y=520, anchor=tkinter.NW)
    # button.pack()

    window.mainloop()