import os
import sys

def changer(a, b):
    print("=== Before pass arguments ===")
    print(a)
    print(b)
    a = 2
    b[0] = 'spam'
    print("== After modified arguments ===")
    print(a)
    print(b)

X = 1
L = [1, 2]
changer(X, L)

print("=== Outside Area ===") 
print("X= " + str(X) + ", L= " + str(L))
#print("X= " + str(X))
#print("L= " + str(L))

