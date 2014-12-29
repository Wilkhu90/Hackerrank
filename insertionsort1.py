N=int(input())
AR=list(map(int, input().split()))
for i in reversed(range(1,N)):
    while AR[i]<AR[i-1]:
        temp=AR[i]
        AR[i]=AR[i-1]
        print("".join(str(item) + " " for item in AR))
        AR[i-1]=temp
print("".join(str(item) + " " for item in AR))
