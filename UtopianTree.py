#! /usr/bin/python
num_test=int(input())
for counter in range(num_test):
    G_cycle=int(input())
    output=1
    for i in range(G_cycle):
        if i%2==0:
            output*=2
        else:
            output+=1
    print(output)    
