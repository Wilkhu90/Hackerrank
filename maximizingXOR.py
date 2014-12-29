#!/usr/bin/python3
def maxXor(l, r):
    Xor_list=[]
    for i in range(l,r+1):
        for j in range(i,r+1):
            Xor_list.append(i^j)
            
    Xor_list.sort()
    return Xor_list[-1]
                       
if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(maxXor(l, r))
