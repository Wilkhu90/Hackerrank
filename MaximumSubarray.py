def max_sum(l):
    current_sum=0
    current_index=-1
    best_sum=0
    best_start_index=-1
    best_end_index=-1
    new_sum=0
    for j in range(len(l)):
        if l[j]<0:
            best_sum,new_sum=l[0],l[0]
        else:
            for i in range(len(l)):
                val=current_sum+l[i]
                if val>0:
                    if current_sum==0:
                        current_index=i
                    current_sum=val
                else:
                    current_sum=0
                if current_sum>best_sum:
                    best_sum=current_sum
                    best_start_index=current_index
                    best_end_index=i
                
                
            new_sum=sum(x for x in l[0:len(l)] if x>=0)   
            break
    print(best_sum,new_sum)      
            
TC=int(input())
for case in range(TC):
    N=int(input())
    lis=list(map(int, input().split()))
    max_sum(lis)
