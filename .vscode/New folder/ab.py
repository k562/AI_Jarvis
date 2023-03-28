n=int(input())
for i in range(1,n+1):
    l=""
    r=""
    for j in range(1,i):   
        if(j%2==0):
            l=l+"A"
            r="A"+r
        else :
            l=l+"B"
            r="B"+r
    res=r+"A"+l
    print(res)