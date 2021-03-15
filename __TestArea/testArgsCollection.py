import os
import sys

#def printData(*, test=99)
def printData(*args, test=99):
    print(*args)
    print(test)

def printData2(*, test=3):
    print(*name)
    print(test)

printData(1,3,5)
print("\n")
printData(1,1)
print("\n")
printData(3,6,test=8)
print("\n")
printData2(91,92,test=1)

