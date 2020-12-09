import os
import sys

def maker(N):
    def action(X):
        return X ** N
    return action

if len(sys.argv) < 2 :
    print("You need input two parameter(fmt : number ")
    print("syntax : C:\python testFactoryFun.py 5 ")
    sys.exit()

num = int(sys.argv[1])


f = maker(num)
print(f)
print("f(3)=" + str(f(3)))
print("f(4)=" + str(f(4)))
