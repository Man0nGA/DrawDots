import turtle as t
import time

def square(x):
    y = x ** 2
    return y


def add_list(l, val):
    l.append(val)


def display_val(inf, sup):
    for i in range(inf, sup + 1):
        print(i)


def step(deb, fin):
    while fin < deb:
        fin = int(input("Enter integer: "))
    s = int(input("Enter an integer: "))
    i = deb
    while i < fin:
        print(i)
        i = i + s


def even(val):
    if val % 2 == 0:
        return True
    else:
        return False


def maxi(a, b, c):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m


def prime(a):
    prim = True
    i = 2
    while prim and i < a:
        if a % i == 0:
            prim = False
        i += 1
    return prim


def somme(l):
    som = 0
    for i in range(len(l)):
        som += l[i]
    return som


def position(l, a):
    for i in range(len(l)):
        if a == l[i]:
            return i
    return -1


def unique(l):
    l1 = []
    for i in range(len(l)):
        if l[i] not in l1:
            l1.append(l[i])
    return l1


def reverse(s):
    s = s[::-1]
    return s


def vowel(s):
    l = ['a', 'e', 'u', 'i', 'o', 'y']
    v = 0
    for e in s:
        if e in l:
            v += 1
    return v


def dbl(m):
    for i in range(0, len(m), 2):
        for j in range(len(m[i])):
            m[i][j] *= 2
    return m


def mix(l, l1):
    i = 0
    l3 = []
    while i < len(l) and i < len(l1):
        l3.append(l1[i])
        l3.append(l[i])
        i += 1
    while i < len(l):
        l3.append(l[i])
        i += 1
    while i < len(l1):
        l3.append(l1[i])
        i += 1
    return l3


def draw_dots(n):
    t.up()
    t.goto(0, -320)
    for i in range(n):
        t.forward(20)
        t.dot(10)
        t.left(360/n)
    time.sleep(10)
