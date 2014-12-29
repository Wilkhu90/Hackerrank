def insertionSort(A):
    for i in range(1,N):
        for j in range(0,i):
            if A[i]<A[j]:
                temp=A[i]
                for c in reversed(range(j,i)):
                    A[c+1]=A[c]
                A[j]=temp
                break
        print("".join(str(item) + " " for item in A))    
    
N=int(input())
AR=list(map(int, input().split()))    
insertionSort(AR)
