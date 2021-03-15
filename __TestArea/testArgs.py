import os

def f(*args):
    print(args)

def f2(**args):
    print(args)

def f3(a, *pargs, **kargs):
    print(a, pargs, kargs)

def f4(a, **args):
    print(a, args)


f(1, 2, 3, 4, 5)

f4(1, c=3, b=2)
f4(3, xy=11, az=9, f=7)

f2(a=1, b=2, d=3)

f3(1, 2, 3, x=1, y=2)

