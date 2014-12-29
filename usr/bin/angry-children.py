#! /usr/bin/python
N=int(input())
a=[]
K=int(input())
for i in range(N):
    a.append(int(input()))
a.sort()
print(min(a[i + K - 1] - a[i] for i in range(0, N - K - 1)))
