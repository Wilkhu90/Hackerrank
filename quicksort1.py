def partition(AR):
    AR1=[]
    AR2=[]
    for i in range(N):
        if AR[i]<AR[0]:
            AR1.append(AR[i])
        if AR[i]>AR[0]:
            AR2.append(AR[i])
    AR1.append(AR[0])
    print(" ".join(map(str,AR1+AR2)))

N=int(input())
AR=list(map(int, input().split()))          
partition(AR)
