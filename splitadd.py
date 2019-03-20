try:
    n=input().split(" ")
    l=input().split(" ")
    sum=0
    if(len(l)==int(n[0])):
        for i in range(int(n[1])):
            sum=sum+int(l[i])
    print(sum)
except:
    print("")
