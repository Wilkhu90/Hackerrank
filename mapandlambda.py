N=int(input())

if (N>=0 and N<=15):
    lis=[0,1]
    a=lis[0]
    b=lis[1]
    for i in range(N-2):
        c=a+b
        a,b=b,a+b
        lis.append(c)
    
cube = lambda a:a*a*a
print(list(map(cube, lis)))
