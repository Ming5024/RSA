#!/usr/bin/python3
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

def deRSA():
    d = text_d.get("1.0", "end-1c")
    d = int(d)
    n = text_n.get("1.0", "end-1c")
    n = int(n)
    #print('d =', d)
    #print('n =', n)
    ciphernum = ciphertextOutput.get("1.0", "end-1c")
    i = 0
    cipher_temp = ''
    result_cipher = ''
    while(i < len(ciphernum)):
        if(ciphernum[i] == ','):
            cipher_temp = int(cipher_temp)
            #print('ciphertext1 =', cipher_temp)
            plaintext1 = decrypt(cipher_temp, d, n)
            #print('plaintext1 =', plaintext1)
            temp_add = 0
            plaintext2 = str(plaintext1)
            plaintext3 = ''
            while(len(plaintext2) % 100 != 0):
                temp_add += 1
                plaintext2 += ' '
            for x in range(0, temp_add):
                plaintext3 += '0'
            plaintext3 += str(plaintext1)
            result_cipher += str(plaintext3)

            cipher_temp = ''
            i += 1
            continue
        cipher_temp += ciphernum[i]
        i += 1

    #print(cipher_temp)
    #cipher_temp = int(cipher_temp)
    #plaintext1 = decrypt(cipher_temp, d, n)
    #print(plaintext1)
    #result_cipher += str(plaintext1)
    #print (result_cipher)
    #print (len(result_cipher))
    i = 0
    final_plain = ''
    while i < len(result_cipher):
        temp_result_plain = ''
        if(result_cipher[i] == '8'):
            i += 1
            for x in range(0, 2):
                if(i >= len(result_cipher)):
                    break
                temp_result_plain += result_cipher[i]
                i += 1
        elif(result_cipher[i] == '9'):
            i += 1
            for x in range(0, 5):
                if (i >= len(result_cipher)):
                    break
                temp_result_plain += result_cipher[i]
                i += 1
        else:
            for x in range(0, 3):
                if (i >= len(result_cipher)):
                    break
                temp_result_plain += result_cipher[i]
                i += 1
        #print('temp_result_plain =', temp_result_plain)
        #print(chr(int(temp_result_plain)))
        if(int(temp_result_plain) == 0):
            break
        final_plain += chr(int(temp_result_plain))


    #print (result_plain)
    #result_plain = result_plain.decode('utf-8')
    plaintextOutput.delete(1.0, tkinter.END)
    plaintextOutput.insert(1.0, final_plain)


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title('RSA解密器')
    window.geometry('600x640')

    l1 = tkinter.Label(window, text='d:', font=("Monospace", 11), width=15, height=2)
    l1.pack()

    text_d = tkinter.Text(window, font=("Helvetica", 12), width=55, height=6)
    text_d.pack()

    l2 = tkinter.Label(window, text='n:', font=("Monospace", 11), width=15, height=2)
    l2.pack()

    text_n = tkinter.Text(window, font=("Helvetica", 12), width=55, height=6)
    text_n.pack()

    l3 = tkinter.Label(window, text='Ciphertext:', font=("Monospace", 11), width=20, height=2)
    l3.pack()

    ciphertextOutput = tkinter.Text(window, font=("Helvetica", 12), width=55, height=7)
    ciphertextOutput.pack()

    l4 = tkinter.Label(window, text='Plaintext:', font=("Monospace", 11), width=20, height=2)
    l4.pack()

    plaintextOutput = tkinter.Text(window, font=("Helvetica", 12), width=55, height=7)
    plaintextOutput.pack()

    button = tkinter.Button(window, text="Decrypt", font=("Monospace", 12), width=15, height=2, command=deRSA)
    button.place(x=200, y=580, anchor=tkinter.NW)
    # button.pack()

    window.mainloop()