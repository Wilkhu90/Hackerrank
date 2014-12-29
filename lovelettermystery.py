#! /usr/bin/python

def Count_Make_Palindrome(Str):
    Counter=0
    mid=int((len(Str)/2))
    if len(Str)%2!=0:
        Str=Str.replace(Str[mid],"")   
    i,j=mid-1,mid
    while i>=0 and j<=len(Str):
        if Str[i] != Str[j]:
            if ord(Str[i])>ord(Str[j]):
                Counter+=ord(Str[i])-ord(Str[j])
            else:
                Counter+=ord(Str[j])-ord(Str[i])
        i-=1
        j+=1
    return Counter

Num_exec=int(input())    
for i in range(Num_exec):
    String=input()
    Cnt=Count_Make_Palindrome(String)
    print(Cnt)
