#!/usr/bin/python

TC=int(input())

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(TC):
    num=int(input())
    for j in range(100000):
        if(num==fib(j)):
            print('IsFibo')
            break
        elif (fib(j)>num):
            print('IsNotFibo')
            break
            
        
